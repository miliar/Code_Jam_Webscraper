
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<cstdio>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

#define mem(a, b) (memset(a, b, sizeof(a)))
#define pb push_back
#define all(v) v.begin(), v.end()
#define rall(v) v.rbegin(), v.rend()
#define rep(i, m) for (ll i = 0; i < (ll)(m); i++)
#define rep2(i, n, m) for (ll i = n; i < (ll)(m); i++)
typedef long long ll;
typedef pair<ll, ll> pii;

const ll oo = (ll) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

ll multi(ll a, ll b) {
    ll flag = 1;
    if (a * b < 0) flag = -1;
    a = abs(a); b = abs(b);
    ll res;
    if (a == 1) {
        res = flag * b;
    } else if (b == 1) {
        res = flag * a;
    } else if (a == 2) {
        if (b == 2) res = flag * -1;
        else if (b == 3) res = flag * 4;
        else res = flag * -3;
    } else if (a == 3) {
        if (b == 2) res = flag * -4;
        else if (b == 3) res = flag * -1;
        else res = flag * 2;
    } else {
        if (b == 2) res = flag * 3;
        else if (b == 3) res = flag * -2;
        else res = flag * -1;
    }
    return res;
}

char L[10010];
ll b[10010];
int main(void) {
    int T, cas = 1;
    scanf("%d", &T);
    while (T--) {
        ll X;
        int len;
        scanf("%d %lld", &len, &X);
        scanf("%s", L);
        for (ll i = 0; i < len; i++) {
            if (L[i] == 'i') L[i] = '2';
            else if (L[i] == 'j') L[i] = '3';
            else L[i] = '4';
        }

        printf("Case #%d: ", cas++);
        ll tmp = L[0] - '0';
        b[0] = tmp;
        for (ll i = 1; i < len; i++) {
            tmp = multi(tmp, L[i]-'0');
            b[i] = tmp;
        }
        ll z = 1;
        ll cc = X; if (cc > 0) cc %= 4;
        for (ll ll = 0; ll < cc; ll++) z = multi(z, tmp);
        if (z != -1) {
            printf("NO\n");
            continue;
        }

        bool flag = false;
        for (ll i = 0; i < 4 && i < X; i++) {

            for (ll j = 0; j < len; j++) {
                ll x = 1;
                for (ll ii = 0; ii < i; ii++) x = multi(x, tmp);
                x = multi(x, b[j]);
                if (x != 2) continue;

                for (ll k = i; k < i+4 && k < X; k++) {
                    for (ll l = (k==i ? j+1 : 0); l < len; l++) {
                        ll y = 1;
                        for (ll kk = 0; kk < k%4; kk++) y = multi(y, tmp);
                        y = multi(y, b[l]);

                        if (y != 4) continue;
                        flag = true;
                        goto M;
                    }
                }
            }
        }
M:
        if (flag) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
