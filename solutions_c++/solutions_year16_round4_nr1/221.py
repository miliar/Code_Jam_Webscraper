#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define FOR(i, x, y) for(int i = x; i < y; ++ i)
#define pb push_back
#define mk make_pair

int n, R, P, S;
string ans;

void get(int t, string a, int p, int r, int s){
    if (t == n){
        if (p == P && r == R && s == S){
            FOR(i,0,n){
                int m = a.size();
                int z = 1 << i;
                for (int k = 0; k < m; k += z * 2){
                    if (a.substr(k + z, z) < a.substr(k, z)){
                        FOR(j,0,z)
                            swap(a[k+j], a[k+z+j]);
                    }
                }
            }
            if (ans == "" || a < ans)
                ans = a;
        }
        return;
    }
    int m = a.size();
    string b = "";
    FOR(i, 0, m){
        if (a[i] == 'P')
            b += "PR";
        if (a[i] == 'R')
            b += "RS";
        if (a[i] == 'S')
            b += "PS";
    }
    get(t + 1, b, s + p, p + r, r + s);
}

void solve() {
    scanf("%d%d%d%d",&n,&R,&P,&S);
    ans = "";
    get(0, "P", 1, 0, 0);
    get(0, "R", 0, 1, 0);
    get(0, "S", 0, 0, 1);
    if (ans == "")
        puts("IMPOSSIBLE");
    else
        puts(ans.c_str());
}

int main() {
#ifdef LOCAL
    freopen("in","r",stdin);
#endif
    int T, Case = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++Case);
        solve();
    }
    return 0;
}
