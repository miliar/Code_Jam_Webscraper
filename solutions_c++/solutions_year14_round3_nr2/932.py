#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
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
#define mp(x, y) make_pair(x, y)
#define pb(e) push_back(e)
#define rep(i, b, n) for (int i = b; i < n; ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define iter(c) __typeof((c).begin())
#define each(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define URU(y) (!(y % 4) && y % 100 || !(y % 400))
#define PI 3.1415926535897932384626433
#define ToRadian(r) ((r)/180.0*PI)
#define ToDegree(r) ((r)*180.0/PI)

using namespace std;

typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef long long LINT;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<LINT> VL;
typedef vector<VL> VVL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef ostringstream OSS;
typedef istringstream ISS;
typedef vector<string> VS;

// 4, 8, 五目
int dx[] = { 0, 0, -1, 1 }, dy[] = { -1, 1, 0, 0 };
//int dx[] = { 0, 0, -1, 1, -1, 1, -1, 1 }, dy[] = { -1, 1, 0, 0, -1, -1, 1, 1 };
//int dx[] = { 1, 1, 0, -1 }, dy[] = { 0, 1, 1, 1 };

template <typename T>
string ToString ( T x ) { OSS oss; oss << x; return string(oss.str()); }
template <typename T>
T ToInteger ( string s ) { ISS iss; iss.str(s); T x; iss >> x; return x; }


bool check ( string str )
{
	vector<bool> hit( 26, false );
	for ( int i = 0; i < str.size(); ++i ) {
		if ( i && str[i] != str[i - 1] && hit[str[i] - 'a'] ) {
			return false;
		}
		hit[str[i] - 'a'] = true;
	}
	return true;
}

const int MOD = 1000000007;
int n, ans;
VS v;
vector<bool> used;
void rec ( string str, int depth )
{
	if ( depth == n ) {
		ans = ( ans + check( str ) ) % MOD;
		return;
	}
	for ( int i = 0; i < n; ++i ) {
		if ( used[i] ) { continue; }
		used[i] = true;
		rec( str + v[i], depth + 1 );
		used[i] = false;
	}
}

string to ( string str )
{
	string s; s += str[0];
	for ( int i = 1; i < str.size(); ++i ) {
		if ( str[i] != str[i - 1] ) { s += str[i]; }
	}
	return s;
}

int main ( void )
{
	int T;
	cin >> T;
	for ( int t = 1; t <= T; ++t ) {
		cin >> n;
		v = VS( n );
		used = vector<bool>( n, false );
		for ( int i = 0; i < n; ++i ) {
			cin >> v[i];
			v[i] = to( v[i] );
		}
		ans = 0;
		rec( "", 0 );
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

