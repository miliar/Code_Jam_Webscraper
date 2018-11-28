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
	int f = 0;
	FOREACH(i, t)
		o << (f++ ? ", " : ": ") << (*i);
	return o << "]";
}

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p)
{
	return o << "(" << p.F << ", " << p.S << ")";
}

#define MIN(a, b) a = min(a, b)

int main()
{
	cout << fixed << setprecision(7);
	int TC;
	cin >> TC;
	FOR(T, TC)
	{
		cout << "Case #" << T + 1 << ": ";

		ld c, f, x;
		cin >> c >> f >> x;
		ld cur = 0, rat = 2;
		ld bsf = x / rat;
		for(int i = 0; cur < bsf; i++)
		{
			cur += c / rat;
			rat += f;
			MIN(bsf, cur + x / rat);
		}

		cout << bsf << endl;
	}
	return 0;
}
