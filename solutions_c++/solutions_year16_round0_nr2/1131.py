#include <bits/stdc++.h>

#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define uniq(c) sort(all((c))), (c).resize(unique(all((c))) - (c).begin())
#define lobo(c, x) (int) (lower_bound(all((c)), (x)) - (c).begin())
#define upbo(c, x) (int) (upper_bound(all((c)), (x)) - (c).begin())
#define R(i,a,b)  for (int i=a; i<=b; i++)
#define Re(i,a,b) for (int i=a; i>=b; i--)
#define tr(i,a) for (__typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define tes cout << "test" << endl, fflush(stdout);
#define cincout ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define print(_v) cout << #_v << " : "; for (auto _i : _v) cout << _i <<", "; cout << endl;

#define pb push_back
#define mt make_tuple
#define mp make_pair
#define x first
#define y second

#define mod 1000000007
#define inf 1000111222
#define eps 1e-9
#define endl "\n"

using namespace std;

typedef long long int64;
typedef pair<int,int> ii;

int T, n;
bool bol[10];

int main () {
    cincout;
    cin >> T;

    R(tc,1,T) {
        string s;
        cin >> s;
        int ans = 0;
        bool ada = false;
        s += '+';

        for (char c : s) {
            if (c == '-') ada = true;
            else if (ada) ans += 2, ada = false;
        }

        if (s[0] == '-' and ans > 0) ans--;

        cout << "Case #" << tc << ": " << ans << endl;
    }
}