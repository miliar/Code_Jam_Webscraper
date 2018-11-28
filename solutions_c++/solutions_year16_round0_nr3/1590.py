#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int p[1000000], pc;
int lsp[10000100];
int ans[15];

#define one(x,i) (((x)&(1LL<<(i))) == 0 ? 0 : 1)

long long prime(long long x){
   if (x < 10000000) return x == p[lsp[x]-1] ? 0 : p[lsp[x]-1];
   else {
        for (int q = 0; q < pc && p[q]*1LL*p[q] <= x; q++)
            if (x % p[q] == 0) return p[q];
        return 0;
   }
}

void solve(){
    int n, m;
    cin >> n >> m;
    if (n <= 16){
        for (long long i = (1<<n); i > 0; i--){
            if (!one(i,0) || !one(i,n-1)) continue;
            memset(ans, 0, sizeof(ans));
            bool ok = 1;
            for (int j = 2; j <= 10 && ok; j++){
                long long cur = 0;
                long long pw = 1;
                for (int q = n-1; q >= 0; q--, pw *= j)
                    if (one(i,q)) cur += pw;
                ans[j] = prime(cur);
     //           cout << cur << "," << ans[j] << " ";
                if (ans[j] == 0) ok = 0;
            }
          //  cout << " x ";
           // cout << ok << ": ";
            if (ok) {
                m--;
     
                for (int q = 0; q < n; q++)
                    cout << (one(i,q) ? 1 : 0);
                cout << " ";
                for (int q = 2; q <= 10; q++)
                    cout << ans[q] << " ";
                cout << endl;
                if (!m) return;
            }
        }
    }else{
        for (long long i = (1LL<<n)-1; i > 0; i--){
            if (!one(i,0) || !one(i,n-1)) continue;
            memset(ans, 0, sizeof(ans));
            bool ok = 1;
            
            for (int j = 2; j <= 10; j++){
                for (int xx = 0; xx < 25; xx++){ 
                    int x = p[xx];
                    int cur = 0;
                    int pw = 1;
                    for (int q = n-1; q >= 0; q--, pw *= j, pw %= x)
                        if (one(i,q)) cur += pw, cur %= x;
                    if (cur == 0) {ans[j] = x;break;}
                }
            }
            for (int j = 2; j <= 10; j++)
                if (ans[j] == 0) ok = 0;
            if (ok) {
                m--;
     
                for (int q = 0; q < n; q++)
                    cout << (one(i,q) ? 1 : 0);
                cout << " ";
                for (int q = 2; q <= 10; q++)
                    cout << ans[q] << " ";
                cout << endl;
                if (!m) return;
            }
        }
 
    }
}

int main()
{
    pc = 0;

    for (int i = 2; i < 10000000; i++){
        if (!lsp[i]) p[pc++] = i, lsp[i] = pc;
        for (int j = 0; j < lsp[i]; j++)
            if (p[j]*1LL*i < 10000000) lsp[p[j]*i] = j+1;
            else        break;
    }
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ":\n";
        solve();
    }
    return 0;
}
