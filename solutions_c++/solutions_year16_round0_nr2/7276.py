// Yerzhan Gapurinov

#include <bits/stdc++.h>
#define ull unsigned ll
#define mp make_pair
#define F first
#define S second
#define ll long long
#define yerzhan gapurinov
#define ld long double
#define pb push_back
#define pll pair<ll, ll>
#define pii pair <int, int>
#define all(v) (v.begin(), v.end())


using namespace std;

const int INF = 1e9 + 7;
const int MXN = 1e6 + 7 ;
const double EPS = 1e-9;
const double PI = acos(-1);

ll n;
ll a[MXN], b[MXN];
string s;
set <int> S;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
   //freopen("modern-art.in", "r", stdin);
   // freopen("modern-art.out", "w", stdout);
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cin >> s;
        ll cnt =  0;
        for(int j = 0; j < s.size(); j++) {
            if(j && s[j] != s[j-1]){
                cnt++;
            }
        }
        if(s[s.size()-1] == '-') cnt++;
        cout << "Case #" << i << ": " << cnt << "\n";
    }

    return 0;
}
