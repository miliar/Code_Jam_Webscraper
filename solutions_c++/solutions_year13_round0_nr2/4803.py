#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPF(i, a, b) for (int i = (a); i <= (b); ++i)
#define REPD(i, a, b) for (int i = (a); i >= (b); --i)
const int maxint = -1u>>1;
int t, n, m;
int x[110][110];

int main() {
        freopen("b.in", "r", stdin);
        freopen("b.out", "w", stdout);
        scanf("%d", &t);
        for (int cas = 1; cas <= t; cas ++) {
                scanf("%d%d", &n, &m);
                int maxn = 0;
                for (int i = 1; i <= n; i ++)
                        for (int j = 1; j <= m; j ++) {
                                scanf("%d", &x[i][j]);
                                maxn = max(maxn, x[i][j]);
                        }
                
                for (int k = 1; k <= maxn; k ++) {
                        for (int i = 1; i <= n; i ++) {
                                int tmp = 0;
                                for (int j = 1; j <= m; j ++) {
                                        tmp = max(tmp, x[i][j]);
                                        if (x[i][j] != 0 && x[i][j] != k) tmp = maxint;
                                }
                                //cout <<tmp<<" "<<k<<endl;
                                if (tmp == k) 
                                        for (int j = 1; j <= m; j ++)
                                                x[i][j] = 0;        
                        }
                        for (int i = 1; i <= m; i ++) {
                                int tmp = 0;
                                for (int j = 1; j <= n; j ++) {
                                        tmp = max(tmp, x[j][i]);
                                        if (x[j][i] != 0 && x[j][i] != k) tmp = maxint;
                                }
                                //cout <<tmp<<" "<<k<<endl;
                                if (tmp == k)
                                        for (int j = 1; j <= n; j ++)
                                                x[j][i] = 0;
                        }
                }
                
                bool flag = true;
                for (int i = 1; i <= n; i ++)
                        for (int j = 1; j <= m; j ++)
                                if (x[i][j] != 0) {
                                        flag = false;
                                        break;
                                }
                
                printf("Case #%d: ", cas);
                if (flag) cout <<"YES"<<endl; else cout <<"NO"<<endl;
        }
    
        return 0;
}














