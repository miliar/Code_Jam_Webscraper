#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int a[1000][3];
int par[1000];

void init(int n) {
    int i;
    
    for (i = 0; i < n; i++) par[i] = i;
}

int find(int x) {
    if (par[x] == x) return x;
    return par[x] = find(par[x]);
}

void unite(int x, int y) {
    x = find(x);
    y = find(y);
    
    if (x == y) return;
    
    par[x] = y;
}

double dist(int x, int y) {
    return sqrt((a[x][0] - a[y][0]) * (a[x][0] - a[y][0]) + (a[x][1] - a[y][1]) * (a[x][1] - a[y][1]) + (a[x][2] - a[y][2]) * (a[x][2] - a[y][2]));
}

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int n, j, k, l;
        vector <pair<double, pair<int, int> > > v;
        
        scanf("%d %*d", &n);
        
        for (j = 0; j < n; j++) scanf("%d %d %d %*d %*d %*d", &a[j][0], &a[j][1], &a[j][2]);
        
        for (j = 0; j < n; j++) {
            for (k = j + 1; k < n; k++) {
                v.push_back(make_pair(dist(j, k), make_pair(j, k)));
            }
        }
        
        sort(v.begin(), v.end());
        
        init(n);
        
        for (j = 0; j < v.size(); j++) {
            unite(v[j].second.first, v[j].second.second);
            
            if (find(0) == find(1)) break;
        }
        
        printf("Case #%d: %.12lf\n", i + 1, v[j].first);
    }
    
    return 0;
}
