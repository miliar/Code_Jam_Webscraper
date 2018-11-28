#include <bits/stdc++.h>

#define left nadnlassad
#define right asdaslknd
#define y1 kjdajasjdsas

#define pb push_back
#define mp make_pair
#define mt make_tuple

#define f first
#define s second

#define ll long long
#define ld long double
#define ull unsigned ll

#define _hash pair<ll, ull>
#define pii pair<int, int>
#define prr pair<pii, pii>

#define sqr(x) ((x) * 1LL * (x))

#define vec vector<int>
#define sz(v) int(v.size())
#define all(v) v.begin(), v.end()
#define endl "\n"
#define _bits(x) __builtin_popcountll(x)

using namespace std;

void rf() {
   #define fname "field"
   #ifdef SONY
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
   #else
//      freopen(fname".in", "r", stdin);
//      freopen(fname".out", "w", stdout);
   #endif //SONY
}

const int nx[8] = {2, -2, -2, 2, 1, 1, -1, -1};
const int ny[8] = {1, 1, -1, -1, 2, -2, -2, 2};

const ll LINF = (ll) 3e18;
const int INF = 1e9 + 7;

const int N = 1e5 + 100;
const int MAXN = 5e7 + 50;
const double EPS = 1e-9, PI = 2 * acos(0.0);
bool to_back[1001];

int main() {
   srand(time(0));
   //ios_base::sync_with_stdio(0), cin.tie(0);
   rf();
   int t;
  	string s;
  	cin >> t;
  	for(int T = 1; T <= t; T++) {
  		cin >> s;
  		string res = "";
  		for(int i = sz(s) - 1; i >= 0; i--)
         to_back[i] = 0;
  		for(int i = sz(s) - 1; i >= 0; i--) {
  			int id = i;
  			for(int j = i; j >= 0; j--)
  				if(s[j] > s[id])
  					id = j;
  			for(int j = i; j > id; j--)
  				to_back[j] = 1;
  			i = id;
  		}
  		for(int i = 0; i < sz(s); i++) {
  			if(to_back[i]) {
  				res += s[i];
  			} else {
  				res = s[i] + res;
  			}
  		}
  		cout << "Case #" << T << ": " << res << endl;
  	}
   return 0;
}
