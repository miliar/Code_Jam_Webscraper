#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>
#include <set>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <valarray>
#include <numeric>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cassert>
#include <bitset>

#define show(x) cerr << "# " << #x << " = " << (x) << endl

#define FR(i, a, b) for(__typeof(a) i = a; i != b; i++)
#define FOR(i, n) for(int i = 0; i < n; i++)
#define FOREACH(i, t) FR(i, t.begin(), t.end())
#define SZ(x) ((int) (x).size())
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef complex<double> point;

template<class T> ostream& operator << (ostream &o, const vector<T> &t)	
{
	o << "[" << SZ(t);
	bool f = false;
	FOREACH(i, t)
		o << (f++ ? ", " : ": ") << (*i);
	return o << "]";
}

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p)
{
	return o << "(" << p.F << ", " << p.S << ")";
}

const int MAXN = 200 + 10;
int a[MAXN][MAXN];
bool o[MAXN][MAXN];

int main()
{
	int TC;
	cin >> TC;
	FOR(T, TC)
	{
		bool can = true;
		memset(o, 0, sizeof o);

		int n, m;
		cin >> n >> m;
		FOR(i, n)
			FOR(j, m)
				cin >> a[i][j];

		FOR(i, n)
		{
			vector<int> v;
			FOR(j, m)
				v.PB(a[i][j]);
			int x = *max_element(v.begin(), v.end());
			FOR(j, m)
				if(a[i][j] == x)
					o[i][j] = true;
		}

		FOR(j, m)
		{
			vector<int> v;
			FOR(i, n)
				v.PB(a[i][j]);
			int x = *max_element(v.begin(), v.end());
			FOR(i, n)
				if(a[i][j] == x)
					o[i][j] = true;
		}

		FOR(i, n)
			FOR(j, m)
				can &= o[i][j];

		cout << "Case #" << T + 1 << ": " << (can ? "YES" : "NO") << endl;
	}
	return 0;
}
