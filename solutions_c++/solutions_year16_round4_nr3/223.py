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

const int MAXn = 100 + 5;
int n, m, k;
int ar[MAXn];
int num[MAXn][MAXn], b[MAXn][MAXn], ans[MAXn][MAXn];
map<int, int> mp;
int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int DFS(int i, int j, int x) {
//	cerr << "GO " << i << ' ' << j << ' ' << x << endl;
	i += dir[x][0];
	j += dir[x][1];
	if(i<1 || i>n || j<1 || j>m) {
//		cerr << "DONE " << i << ' ' << j << endl;
		return num[i][j];
	}
	if(b[i][j]) {
		if(x==0)
			x = 3;
		else if(x==1)
			x = 2;
		else if(x==2)
			x = 1;
		else
			x = 0;
	}
	else {
		if(x==0)
			x = 1;
		else if(x==1)
			x = 0;
		else if(x==2)
			x = 3;
		else
			x = 2;
	}
	return DFS(i, j, x);
}

int main()
{
	ios_base::sync_with_stdio(false);

	int TC; cin >> TC;
	for(int TestCase=1; TestCase<=TC; ++TestCase) {
		cin >> n >> m;
		k = 2*(n + m);
		mp.clear();
		for(int i=0; i<k; i+=2) {
			cin >> ar[i] >> ar[i+1];
			mp[ar[i]] = ar[i+1];
			mp[ar[i+1]] = ar[i];
		}

		rep(i, n+2) rep(j, m+2)
			num[i][j] = 0;
		int cur = 1;
		for(int i=1; i<=m; ++i)
			num[0][i] = cur++;
		for(int i=1; i<=n; ++i)
			num[i][m+1] = cur++;
		for(int i=m; i; --i)
			num[n+1][i] = cur++;
		for(int i=n; i; --i)
			num[i][0] = cur++;


/*			rep(i, n+2) {
				rep(j, m+2)
					cerr << num[i][j];
				cerr << endl;
			}*/

		bool dnn = false;
		int p = n*m;
		rep(mask, (1<<p)) {
			int z = 0, i = 1, j = 1;
			while(z<p) {
				b[i][j] = mask & (1<<z);
				j++;
				if(j==m+1)
					j=1, i++;
				++z;
			}

/*			cerr << "NICE " << endl;
			rep(i, n+2) {
				rep(j, m+2)
					cerr << b[i][j];
				cerr << endl;
			}*/

			bool ok = true;
			for(int i=1; i<=m && ok; ++i)
				if(DFS(0, i, 1) != mp[num[0][i]])
					ok = false;
			for(int i=1; i<=n && ok; ++i)
				if(DFS(i, m+1, 2) != mp[num[i][m+1]])
					ok = false;
			for(int i=m; i && ok; --i)
				if(DFS(n+1, i, 3) != mp[num[n+1][i]])
					ok = false;
			for(int i=n; i && ok; --i)
				if(DFS(i, 0, 0) != mp[num[i][0]])
					ok = false;
//			cerr << "OK ? " << ok << endl;
			if(ok) {
				dnn = true;
				rep(i, n+2) rep(j, m+2)
					ans[i][j] = b[i][j];
				break;
			}
		}

		cout << "Case #" << TestCase << ":" << endl;
		if(!dnn)
			cout << "IMPOSSIBLE" << endl;
		else {
			rep(i, n) {
				rep(j, m)
					if(ans[i+1][j+1])
						cout << '/';
					else
						cout << '\\';
				cout << endl;
			}
		}
	}

	return 0;
}







