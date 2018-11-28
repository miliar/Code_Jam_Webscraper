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

const int MAXn = 1<<14 + 10;
int n, r, p, s;
int cnt[3][20][3];
string good[3][20];
string Strs[] = {"P", "R", "S"};


int main()
{
	ios_base::sync_with_stdio(false);

	rep(i, 3) {
		good[i][0] = Strs[i];
		cnt[i][0][i] = 1;
	}
	for(int j=1; j<=12; ++j)
		rep(i, 3) {
			int x = i;
			int y = (i + 1) % 3;
			string s1 = good[x][j-1],
				   s2 = good[y][j-1];
			if(s1 > s2)
				swap(s1, s2);
			good[i][j] = s1 + s2;
			rep(k, 3)
				cnt[i][j][k] = cnt[x][j-1][k] + cnt[y][j-1][k];
		}

	int TC; cin >> TC;
	for(int TestCase=1; TestCase<=TC; ++TestCase) {
		cerr << TestCase << endl;
		cin >> n >> r >> p >> s;

		int bst = -1;

		rep(i, 3)
			if(cnt[i][n][0]==p && cnt[i][n][1]==r && cnt[i][n][2]==s) {
				if(bst==-1 || good[i][n] < good[bst][n])
					bst = i;
			}
			cout << "Case #" << TestCase << ": ";
			if(bst==-1)
				cout << "IMPOSSIBLE";
			else
				cout << good[bst][n];
			cout << endl;
	}

	return 0;
}







