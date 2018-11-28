#include <bits/stdc++.h>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

// Loops
#define REP(i,n)                        for(int i=0;i<(n);i++)
#define REPG(i,n)                       for(i=0;i<(n);i++)
#define FOR(i,a,b)                      for(int i=(a);i<=(b);i++)
#define FORD(i,a,b)                     for(int i=(a);i>=(b);i--)

#define inf                             10e9 // 1 billion, safer than 2B for Floyd Warshall’s
#define mod                             1000000007
#define pb                              push_back
#define mp                              make_pair

// Some common useful functions
#define sqr(x)                          ((x)*(x))
#define rnd(d)                          (int)((double)d + 0.5)
#define sz(x)                           ((int)(x).size())
#define rite(x)                         freopen(x,"w",stdout);
#define read(x)                         freopen(x,"r",stdin);
#define vecIsPresent(vec, x)            find(vec.begin(), vec.end(), x) != vec.end();

int n, t, ans;
int main() {
	freopen("small", "r", stdin);
 	freopen("output.txt", "w", stdout);

    cin >> t;

    FOR(x, 1, t) {
        string s;
        cin >> s;
        ans = 0;

        REP(i, s.length()-1) {
            if(s[i]!=s[i+1]) {
                ans++;
            }
        }
        if(s[s.length()-1]=='-') ans++;
        cout <<  "Case #" << x << ": " << ans << endl;
    }

	return 0;
}
