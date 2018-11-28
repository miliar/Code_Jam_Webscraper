#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>

#define FI first
#define SE second
#define MP make_pair
#define PB push_back

const int MAXN = 1005;

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;

int tnum, n;
double nao[MAXN], ken[MAXN];
bool mark[MAXN];
int f[MAXN][MAXN];

int main(){
    scanf("%d", &tnum);
    for (int t=1; t<=tnum; t++){
        memset(mark, 0, sizeof mark);
        printf("Case #%d: ", t);
        
        scanf("%d", &n);
        for (int i=1; i<=n; i++) scanf("%lf", &nao[i]);
        for (int i=1; i<=n; i++) scanf("%lf", &ken[i]);
        
        sort(nao+1, nao+n+1);
        sort(ken+1, ken+n+1);
        
        int res1 = 0;
        for (int i=1; i<=n; i++) f[i][i] = nao[n]>ken[i]?1:0;
        for (int L=2; L<=n; L++){
            for (int s=1; s+L-1<=n; s++){
                int e = s+L-1, k = n-L+1;
                f[s][e] = 0;                
                if (nao[k]>ken[e]) f[s][e] = L;
                else {
                    f[s][e] = f[s][e-1];
                    if (nao[k]>ken[s]) f[s][e] = max(f[s][e], f[s+1][e] + 1);
                }
            }
        }
        res1 = f[1][n];
        
        int res2 = 0;
        for (int i=1; i<=n; i++){
            bool found = false;
            int fir = 0;
            for (int j=1; j<=n; j++)
                if (!mark[j]){
                    fir = j;
                    if (ken[j]>nao[i]){
                        mark[j] = true;
                        found = true;                        
                        break;
                    }
                }
            
            if (!found){
                res2++;
                mark[fir] = true;
            }
        }
        
        printf("%d %d\n", res1, res2);
    }
    return 0;
}
