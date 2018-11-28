#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int test, n, m;
ll res[11];
string s;

ll toInt(const string& s, const int& base){
    ll res = 0;
    for (int i = 0; i < s.length(); ++i)
        res = (res * base) + s[i] - '0';
    return res;
}

int main(){
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> test;
    for (int ii = 1; ii <= test; ++ii){
        cin >> n >> m;
        cout << "Case #" << ii << ":\n";
        s = "";
        for (int i = 0; i < n; ++i)
            s.push_back('1');

        for (ll i = 0; m > 0; ++i){
            for (int j = 0; j < n - 2; ++j)
                s[j + 1] = ((i >> (n - 3 - j)) & 1) + '0';

            memset(res, 0, sizeof(res));
            for (int j = 2; j <= 10; ++j){
                ll x = toInt(s, j);
                for (ll k = 2; k * k <= x; ++k)
                if (x % k == 0){
                    res[j] = k;
                    break;
                }
                if (res[j] == 0)
                    break;
            }

            if (res[10] == 0)
                continue;

            --m;
            cout << s;
            for (int j = 2; j <= 10; ++j)
                cout << ' ' << res[j];
            cout << "\n";
        }
    }
    return 0;
}
