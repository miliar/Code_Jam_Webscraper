#include <cstdlib>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int T;
int N, M;
int zip[100];
int path[100];
int res[100];
bool mark[100];
bool mark2[100];

bool mycmp(pair<int,int> a, pair<int,int> b) {
    return zip[a.second] < zip[b.second];
}

int dfs(vector< vector<int> > &adj, int d, int p) {
    if (d == N) {
        for (int i = 0; i < N; i++) printf("%d", zip[res[i]]);
        printf("\n");
        return true;
    }
    memset(mark2, 0, sizeof(bool)*100);
    vector<pair<int,int> > nodes;
    for (int i = p; i >= 0; i--) { 
        int x = path[i];
        for (vector<int>::iterator y = adj[x].begin(); y != adj[x].end(); ++y) {
            if (!mark[*y] && !mark2[*y] ) {
                mark2[*y] = true;
                nodes.push_back(make_pair(i, *y));
            }
        }
    }
    sort(nodes.begin(), nodes.end(), mycmp);
    for (vector<pair<int,int> >::iterator i = nodes.begin(); i != nodes.end(); i++) {
        int tmp = path[(*i).first+1];
        path[(*i).first+1] = (*i).second;
        res[d] = (*i).second;
        mark[(*i).second] = true;
        if (dfs(adj, d+1, (*i).first+1)) {
            return true;
        }
        mark[(*i).second] = false;
        path[(*i).first+1] = tmp;
    }
    return false;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d %d", &N, &M);
        int p = 0;
        memset(mark, 0, sizeof(bool)*N);
        vector< vector<int> > adj(N, vector<int>(0));
        for (int i = 0; i < N; i++) scanf("%d", zip+i);
        for (int i = 0; i < M; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
            x--;
            y--;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }
        int min = 100000;
        int start;
        for (int i = 0; i < N; i++) {
            if (zip[i] < min) {
                min = zip[i];
                start = i;
            }
        }
        path[0] = start;
        p = 0;
        mark[start] = true;
        res[0] = start;
        printf("Case #%d: ", t+1);
        dfs(adj, 1, 0);
    }

    return 0;
}
