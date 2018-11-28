#include <bits/stdc++.h>
using namespace std;
const int N = 1005;

int n , p[N] , deg[N] , res;
vector<int> e[N];
bool v[N];
int f[N];

void dfs(int x , int fa) {
    f[x] = 0;
    for (auto &y : e[x]) {
        if (y != fa && !deg[y]) {
            dfs(y , x);
            f[x] = max(f[x] , f[y] + 1);
        }
    }
}

void work() {
    scanf("%d" , &n);
    for (int i = 1 ; i <= n ; ++ i) {
        e[i].clear();
        deg[i] = v[i] = 0;
        scanf("%d" , &p[i]);
    }
    for (int i = 1 ; i <= n ; ++ i) {
        e[p[i]].push_back(i);
        ++ deg[p[i]];
    }
    queue<int> Q;
    for (int i = 1 ; i <= n ; ++ i) {
        if (deg[i] == 0) {
            Q.push(i);
        }
    }
    while (!Q.empty()) {
        int x = Q.front(); Q.pop();
        int y = p[x];
        if (!-- deg[y]) {
            Q.push(y);
        }
    }
    res = 0; int sum = 0;
    for (int i = 1 ; i <= n ; ++ i) {
        if (deg[i] && !v[i]) {
            vector<int> V;
            int x = i;
            while (!v[x]) {
                v[x] = 1;
                V.push_back(x);
                x = p[x];
            }
            int m = V.size();
            res = max(res , m);
            if (m == 2) {
                dfs(V[0] , 0);
                dfs(V[1] , 0);
                sum += f[V[0]] + f[V[1]] + 2;
            }
        }
    }
    printf("%d\n" , max(res , sum));
}

int main() {
    freopen("in" , "r" , stdin);
    int T , ca = 0;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
