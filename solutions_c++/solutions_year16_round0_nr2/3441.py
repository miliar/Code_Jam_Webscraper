#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int nmax = 150005;
const long double PI = acos(-1.0);
const ll mod = 1e9 + 7;
const long double eps = 1e-6;
int main(){
    //ios_base::sync_with_stdio(0);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll t;
    cin >> t;
    for(int q = 1; q <= t; ++q){
        string s;
        cin >> s;
        int cnt = 0;
        int last = -1;
        for(int i = 0; i < s.size(); ++i) if (s[i] == '-') last = i;
        while(last > -1){
            for(int i = 0; i <= last; ++i){
                if (s[i] == '-') s[i] = '+';
                else s[i] = '-';
            }
            int newlast = -1;
            for(int i = 0; i <= last; ++i){
                if (s[i] == '-') newlast = i;
            }
            last = newlast;
            cnt++;
        }
        printf("Case #%d: %d\n", q, cnt);
    }
    return 0;
}
