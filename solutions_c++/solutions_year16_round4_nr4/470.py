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

const int MAXn = 26;
int n;
int ar[MAXn][MAXn];
int cnt = 0, mn = 10000;

bool check()
{
	rep(i, n) {
		set<int> st;
		int m = 0;
		rep(j, n)
			if(ar[i][j]) {
				++m;
				rep(k, n)
					if(k!=i && ar[k][j]) {
						st.insert(k);
					}
			}
		if(m <= st.size())
			return false;
	}
	return true;
}

void BT(int i, int j)
{
	if(cnt >= mn)
		return;

	if(i==n)
		return BT(0, j+1);
	if(j==n) {
		if(check())
			mn = cnt;
		return;
	}

	BT(i+1, j);
	if(ar[i][j]==0) {
		ar[i][j] = 1;
		++cnt;
		BT(i+1, j);
		--cnt;
		ar[i][j] = 0;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);

	int TC; cin >> TC;
	for(int TestCase=1; TestCase<=TC; ++TestCase) {
		cin >> n;
		rep(i, n) rep(j, n) {
			char c;
			cin >> c;
			ar[i][j] = (c=='1');
		}
		cnt = 0;
		mn = 1000000;
		BT(0, 0);
		cout << "Case #" << TestCase << ": " << mn << endl;
	}

	return 0;
}







