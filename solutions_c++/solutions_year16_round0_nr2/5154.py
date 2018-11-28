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
int n;

int main()
{
	ios_base::sync_with_stdio(false);

	int tt; cin >> tt;
	for(int ii=1; ii<=tt; ++ii) {
		string s;
		cin >> s;
		n = s.size();
		int b = 0, ans = 0;
		for(int i=n-1; i>=0; --i) {
			int x = s[i]=='-';
			if(x+b==1) {
				b = 1 - b;
				++ans;
			}
		}
		cout << "Case #" << ii << ": " << ans << endl;
	}

	return 0;
}





