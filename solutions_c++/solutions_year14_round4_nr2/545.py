#include <bits/stdc++.h>
using namespace std;


#define Size(s) ((int)s.size())
#define rep(i, n) for(int i=1; i<=n; ++i)
#define Foreach(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define F first
#define S second
#define X real()
#define Y imag()
#define MP make_pair

template<class P, class Q> inline bool mmin(P &a, Q b) { if (a > b){ a = b; return true;} return false;}
template<class P, class Q> inline bool mmax(P &a, Q b) { if (a < b){ a = b; return true;} return false;}

typedef long long LL;
typedef pair<int, int> pii;

const int MAXn = 1000 + 5;
int n;
int dp[MAXn][MAXn];
int ar[MAXn], b[MAXn];
int pre[MAXn][MAXn];
map<int, int> mp;
bool mark[MAXn][MAXn];
int f1[MAXn], f2[MAXn];

void init()
{

}

int get(int x, int y)
{
	if(mark[x][y])
		return dp[x][y];
	mark[x][y] = true;
	if(x==n || y==n)
		return dp[x][y] = 0;

	int cur = max(x, y) + 1;

	return dp[x][y] = min(get(cur, y) + f1[cur], get(x, cur) + f2[cur]);
}

int main()
{
	ios_base::sync_with_stdio(false);

	int nq;
	cin >> nq;
	rep(ii, nq) {
		cin >> n;
		rep(i, n)
			cin >> ar[i];
		copy(ar+1, ar+n+1, b+1);
		sort(b+1, b+n+1);
		mp.clear();
		rep(i, n)
			mp[b[i]] = i;
		rep(i, n)
			ar[i] = mp[ar[i]];
		rep(i, n)
			b[ar[i]] = i;

		rep(i, n) {
			f1[i] = f2[i] = 0;
			for(int j=b[i]+1; j<=n; ++j)
				if(ar[j]>i)
					++f2[i];
			for(int j=b[i]-1; j>0; --j)
				if(ar[j]>i)
					++f1[i];
		}

		for(int i=0; i<=n; ++i) for(int j=0; j<=n; ++j) mark[i][j] = 0;

		cout << "Case #" << ii << ": " << min(get(1, 0)+f1[1], get(0, 1)+f2[1]) << endl;
	}

	return 0;
}
