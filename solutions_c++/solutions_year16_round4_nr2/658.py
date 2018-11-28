#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define sz(x) (int((x).size()))
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define F first
#define S second
#define X real()
#define Y imag()
#define all(X) (X).begin(),(X).end()
#define MP make_pair

template<class P, class Q> inline bool mmin(P &a, Q b) { if (a > b){ a = b; return true;} return false;}
template<class P, class Q> inline bool mmax(P &a, Q b) { if (a < b){ a = b; return true;} return false;}

typedef long long LL;
typedef pair<int, int> pii;
typedef complex<double> point;

const int MAXn = 200 + 10;
int n, k;
double pr[MAXn];
int ar[MAXn];
vector<int> v;
int br[MAXn];

double get() {
	double sum = 0;
	rep(i, k)
		br[i] = 0;
	rep(i, k/2)
		br[k-1-i] = 1;
	do {
		double cur = 1.;
		rep(i, k)
			if(br[i])
				cur *= pr[v[i]];
			else
				cur *= 1-pr[v[i]];
		sum += cur;
	}while(next_permutation(br, br+k));
	return sum;
}

int main()
{
	ios_base::sync_with_stdio(false);

	int TC; cin >> TC;
	for(int TestCase=1; TestCase<=TC; ++TestCase) {
		cin >> n >> k;
		rep(i, n)
			cin >> pr[i];
		rep(i, n)
			ar[i] = 0;
		rep(i, k)
			ar[n-1-i] = 1;

		double ans = 0.;
		int ii = 0;
		do {
			v.clear();
			rep(i, n)
				if(ar[i])
					v.push_back(i);
			double res = get();
			ans = max(ans, res);
		}while(next_permutation(ar, ar+n));

		cout << "Case #" << TestCase << ": " << fixed << setprecision(7) << ans << endl;
	}

	return 0;
}







