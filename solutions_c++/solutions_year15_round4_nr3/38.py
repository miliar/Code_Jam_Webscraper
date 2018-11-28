#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-12;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;


namespace MaxFlow
{
    const int N = 100000*2;
    const int M = 100000*2;

    int n, m, x[N], y[N];

    int edgeCount, firstEdge[N], to[M], capacity[M], nextEdge[M], currentEdge[N];
    int source, target, flow, pre[N], sign;

    void addEdge(int u, int v, int w) {
        to[edgeCount] = v;
        capacity[edgeCount] = w;
        nextEdge[edgeCount] = firstEdge[u];
        firstEdge[u] = edgeCount ++;
    }

    void insert(int u, int v, int w)
    {
        addEdge(u, v, w);
        addEdge(v, u, 0);
    }

    int level[N], queue[N];

    bool bfs(int s, int t) {
        memset(level, -1, sizeof(level));
        sign=t;
        level[t] = 0;
        int tail = 0;
        queue[tail ++] = t;
        int head = 0;
        while (head != tail && level[s] == -1) {
            int v = queue[head ++];
            for (int iter = firstEdge[v]; iter != -1; iter = nextEdge[iter]) {
                if (capacity[iter ^ 1] > 0 && level[to[iter]] == -1) {
                    level[to[iter]] = level[v] + 1;
                    queue[tail ++] = to[iter];
                }
            }
        }
        return level[s] != -1;
    }

    inline void push()
    {
        int delta=INT_MAX,u,p;
        for (u=target;u!=source;u=to[p]){
            p=pre[u];
            delta=min(delta,capacity[p]);
            p^=1;
        }

        for (u=target;u!=source;u=to[p]){
            p=pre[u];
            capacity[p]-=delta;
            if (!capacity[p]){
                sign=to[p^1];
            }
            capacity[p^=1]+=delta;
        }
        flow+=delta;
    }

    void dfs(int u) {
        if (u == target) {
            push();
            return;
        }
        for (int &iter = currentEdge[u]; iter != -1; iter = nextEdge[iter]) {
            if (capacity[iter] > 0 && level[u] == level[to[iter]] + 1) {
                pre[to[iter]]=iter;
                dfs(to[iter]);
                if (level[sign]>level[u]) return;
                sign=target;
            }
        }
        level[u]=-1;
    }

    void initNetwork(int nodes)
    {
        n = nodes;
        edgeCount = 0;
        for (int i = 0; i <= n; ++i)
            firstEdge[i] = -1;
    }

    int maxFlow(int s, int t)
    {
        source = s;
        target = t;

        flow=0;
        while (bfs(source, target)) {
            for (int i = 0; i < n; ++ i) {
                currentEdge[i] = firstEdge[i];
            }
            dfs(source);
        }

        return flow;
    }
}

char buffer[100000];

void solve(int test_id) {
    int n;
    cin >> n;
    gets(buffer);
    vector< vector<string> > lines;
    REP(i, n) {
        gets(buffer);
        vector<string> current_line;
        int length = strlen(buffer);
        string word;
        for (int j = 0; j < length; ++j) {
            if (buffer[j] != ' ') {
                word += buffer[j];
            } else {
                current_line.push_back(word);
                word = "";
            }
        }
        assert(word != "");
        current_line.push_back(word);
        lines.push_back(current_line);
    }
    map<string, int> all_words;
    int last_word_id = 0;
    REP(i, n) {
        TR(it, lines[i]) {
            if (!all_words.count(*it)) {
                all_words[*it] = last_word_id++;
            }
        }
    }
    MaxFlow::initNetwork(2 + 2 * n + 2 * last_word_id);
    int source = 2 * n + 2 * last_word_id;
    int target = source + 1;
    REP(i, last_word_id) {
        MaxFlow::insert(2 * n + i, 2 * n + last_word_id + i, 1);
    }
    REP(i, n) {
        TR(it, lines[i]) {
            int wid = all_words[*it];
            // cout << "wid is "<< wid << endl;
            MaxFlow::insert(i, 2 * n + wid, 100000000);
            MaxFlow::insert(2 * n + last_word_id + wid, n + i, 100000000);
        }
        MaxFlow::insert(i, n + i, 100000000);
    }
    MaxFlow::insert(source, 0, 100000000);
    MaxFlow::insert(n + 1, target, 100000000);
    for (int i = 2; i < n; ++i) {
        MaxFlow::insert(source, i, 100000);
        MaxFlow::insert(n + i, target, 100000);
    }
    cout << "Case #" << test_id << ": " << MaxFlow::maxFlow(source, target) - 100000 * (n - 2) << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int test_id = 1; test_id <= tests; ++test_id) {
        solve(test_id);
    }
    return 0;
}