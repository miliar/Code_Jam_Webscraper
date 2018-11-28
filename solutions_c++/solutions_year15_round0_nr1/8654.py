#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define X first
#define Y second
#define rep(i, b, n) for (int i = b; i < n; ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define iter(c) __typeof((c).begin())
#define each(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)

using namespace std;

typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<LL> VL;
typedef vector<VL> VVL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef ostringstream OSS;
typedef istringstream ISS;
typedef vector<string> VS;

//const int INF = ( 1 << 31 ) - 1;
// const LINT INF = ( 1LL << 63 ) - 1LL;

// __builtin_popcount( n )

void solve ( void )
{
	int Smax = 0, ans = 0, now = 0, n = 0;
	string audience = "";

	cin >> Smax >> audience;

	for ( int i = Smax; i >= 0; --i ) {
		if ( audience[i] != '0' ) {
			n = i;
			break;
		}
	}
	
	for ( int i = 0; i <= n; ++i ) {
		if ( now < i ) {
			ans += i - now;
			now += i - now;
		}
		now += audience[i] - '0';
	}

	cout << ans << endl;
}

int main ( void )
{
	// cin.tie( 0 );
	// ios::sync_with_stdio( false );
	int t;
	while ( cin >> t ) {
		for ( int i = 1; i <= t; ++i ) {
			cout << "Case #" << i << ": ";
			solve();
		}
	}
	return 0;
}
