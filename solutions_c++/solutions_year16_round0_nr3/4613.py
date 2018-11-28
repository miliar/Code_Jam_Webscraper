#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

typedef long long ll;

#define pb push_back
#define mp make_pair
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define file freopen("1.txt","r",stdin)
#define llel y1
#define x MAXN


ll n,m,k,l,r,ans,t,j,a[1111];
ll step[111][111];
vector<ll> v;
vector<string> u;
string s;
bool f,g;

string dvoi(ll x){
    string ans = "";

    while(x > 0){
        ans = char((x % 2) + '0') + ans;
        x /= 2;
    }

    return ans;
}

ll solve(string s,ll k){
    reverse(s.begin(),s.end());

    ll x = 0;

    for(ll i = 0; i < s.size(); ++i){
        if (s[i] == '1') x += (step[k][i]);
    }

   // cout << x << "\n";

   ll lel = 0;

    for(ll i = 2; i <= round(sqrt(x)); ++i){
        if (x % i == 0){
            lel = i;
            break;
        }
    }

    return lel;
}

main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("1.txt","w",stdout);

    for(ll i = 2; i <= 10; ++i){
        step[i][0] = 1;
        for(ll j = 1; j <= 33; ++j){
            step[i][j] = step[i][j - 1] * i;
        }
    }

    cin >> t;

    for(ll jj = 1; jj <= t; ++jj){
        cin >> n >> m;

        cout << "Case #" << jj << ":\n";
        l = step[2][n - 1] + 1;
        r = step[2][n] - 1;

        for(ll i = l; i <= r; i += 2){
            s = dvoi(i);
           // cout << s << "\n";
            f = true;
            for(ll j = 2; j <= 10; ++j){
                a[j] = solve(s,j);
                if (!a[j]){
                    f = false;
                    break;
                }
            }
            if (f){
                m--;
                cout << s << ' ';
                for(ll j = 2; j <= 10; ++j){
                    cout << a[j] << ' ';
                }
                if (m) cout << "\n";
            }
            if (!m) break;
        }
    }
}
