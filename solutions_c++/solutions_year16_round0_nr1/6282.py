#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main() {
    //freopen("A_in.txt", "r", stdin);
    freopen("A.out", "w", stdout);
    int cs, T, flag, cnt;
    ll n, i, ans;
    map<ll, bool> rec;
    scanf("%d", &T);
    for(cs = 1; cs <= T; cs ++) {
        rec.clear(), cnt = 0, flag = 0;
        scanf("%lld", &n);
        for(i = 1; i <= 1000; i ++) {
            ll k = (i * n);
            ll T = k;
            while(k) {
                ll p = k % 10;
                if(rec[p] == false) cnt ++, rec[p] = true;
                k /= 10;
            }
            if(cnt == 10) {
                flag = 1;
                ans = T;
                break;
            }
        }
        printf("Case #%d: ", cs);
        if(flag == 1) {
            printf("%lld\n", ans);
        } else {
            printf("INSOMNIA\n");
        }
    }
}
