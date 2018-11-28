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

const int MAXn = 100*1000 + 5;
int mark[20], cnt;

inline void f(int m) {
	while(m) {
		if(!mark[m%10]) {
			--cnt;
			mark[m%10] = 1;
		}
		m /= 10;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);

	int t; cin >> t;
	for(int ii=1; ii<=t; ++ii) {
		int n, m = 0;
		cin >> n;
		fill_n(mark, 10, 0);
		cnt = 10;
		if(n==0)
			cout << "Case #" << ii << ": INSOMNIA" << endl;
		else {
			while(cnt) {
				m += n;
				f(m);
			}
			cout << "Case #" << ii << ": " << m << endl;
		}
	}

	return 0;
}





