#include <bits/stdc++.h>

using namespace std;


#define pb push_back
#define ll long long
#define mp make_pair
#define f first
#define s second
#define pii pair < int, int >
#define pll pair < ll, ll >
#define all(s) s.begin(), s.end()
#define sz(s) (int) s.size()
#define vi vector < int >

const int inf = (int)1e9;
const int mod = (int) 1e9 + 7;


int main () {
    #ifdef LOCAL
    freopen ("a.in", "r", stdin);
    freopen ("a.out", "w", stdout);
    #endif

    int n;
    cin >>n;

    string s;
    for (int ii=0;ii<n;ii++){
        cin >>s;
        int j = sz(s)-1;
        while (j >= 0 && s[j] == '+') j--;
        s = s.substr(0, j + 1);
        int ans = 0;
        for (int i=0;i<sz(s);i++){
            if (i > 0 && s[i] == s[i-1]) continue;
            ans++;
        }
        printf("Case #%d: %d\n", ii+1, ans);
    }

    #ifdef LOCAL
    cerr << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
