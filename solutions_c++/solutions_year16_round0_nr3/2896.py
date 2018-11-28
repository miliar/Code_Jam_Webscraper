#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int nmax = 150005;
const long double PI = acos(-1.0);
const ll mod = 1e9 + 7;
const long double eps = 1e-6;
ll p[11][20];
ll check(string cur, ll j){
    ll dig = 0;
    for(int i = 0; i < cur.size(); ++i){
        dig += (cur[i] - '0') * p[j][i];
    }
    for(ll i = 2; i * i <= dig; ++i){
        if (dig % i == 0){
            return i;
        }
    }
    return -1;
}
int main(){
    //ios_base::sync_with_stdio(0);
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(ll i = 2; i <= 10; ++i){
        p[i][0] = 1;
        for(int j = 1; j <= 18; ++j){
            p[i][j] = p[i][j - 1] * i;
        }
    }
    int t;
    scanf("%d", &t);
    for(int q = 1; q <= t; ++q){
        ll n, J;
        scanf("%I64d%I64d", &n, &J);
        ll en = min(n - 1, 16ll);
        printf("Case #%d:\n", q);
        for(ll i = 0; i < (1ll << en); i += 2){
            if (!J) break;
            string cur = "";
            i |= 1;
            for(int j = 0; j < en; ++j){
                if (i & (1ll << j)) cur += '1';
                else cur += '0';
            }
            for(int j = en; j < n - 1; ++j){
                cur += '0';
            }
            cur += '1';
            int flag = 0;
            vector<ll> v;
            for(int j = 2; j <= 10; ++j){
                ll d = check(cur, j);
                if (d == -1){
                    flag = 1;
                    break;
                }
                else v.push_back(d);
            }
            if (!flag){
                reverse(cur.begin(), cur.end());
                cout << cur << ' ';
                for(int i = 0; i < 9; ++i) printf("%I64d ", v[i]);
                printf("\n");
                J--;
            }
        }
    }
    return 0;
}
