#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstdlib>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define mp make_pair

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)


int mod1 = int(1e9) + 7;

ll a[10100];

int main(){
    cout.precision(9);

	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {

		int n;
		cin >> n;

		forn(i,n) cin >> a[i];

		ll s1=0, s2=0;

		forn(i,n-1) {
			s1+=max(0LL,a[i]-a[i+1]);
		}

		ll maxdiff = 0;
		forn(i,n-1) {
			maxdiff = max(maxdiff, a[i]-a[i+1]);
		}

		forn(i,n-1) s2+= min(a[i], maxdiff);

		cout << "Case #" << cas << ": " << s1 << " " << s2 << endl;
	}

	return 0;
}
