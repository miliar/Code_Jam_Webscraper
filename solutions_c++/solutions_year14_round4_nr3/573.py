#include <bits/stdc++.h>
#define f(i,x,y) for (int i = x; i < y; i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define pii pair<int,int>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define eps (1e-9)
#define oo (1<<30)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; f(i,0,m)f(j,0,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define N 1
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}

int tc,caso;
int m,n,b, J;
int a[505][505];
int dx[] = {1,0,-1,0,1,0,-1,0};
int dy[] = {0,1,0,-1,0,1,0,-1};

bool dfs(int x, int y, int dir) {
//	cout << x << " " << y << endl;
	if (y == n-1) return 1;
	dir += 3;
	f(k,0,4) {
		int dk = (dir + k) % 4;
		int nx = x + dx[dk];
		int ny = y + dy[dk];
		if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
		if (a[nx][ny]) continue;
		a[nx][ny] = J;
		if ( dfs (nx, ny, dk) ) return 1;
//		a[nx][ny] = 0;

//		a[nx][ny] = J;
//		return dfs(nx, ny, dk);
	}
	return 0;
}

int main(){
	cin >> tc;
	while(tc--) {
		cin >> m >> n >> b;
		J = 2;
		clr(a,0);
		vint X,Y;
		f(i,0,b) {
			int x1,y1,x2,y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			X.pb(x1); X.pb(x2+1);
			Y.pb(y1); Y.pb(y2+1);
			for(int x = x1; x <= x2; x++)
				for(int y = y1; y <= y2; y++)
					a[x][y] = 1;
		}
		/*
		set<int> sx(all(X));
		sx.insert(0); sx.insert(m);
		set<int> sy(all(Y));
		sy.insert(0); sy.insert(n);
		int sz = 0;
		map<int,int> mx; FOR(it, sx) mx[*it] = sz++;
		m = sz-1;
		sz = 0;
		map<int,int> my; FOR(it, sy) my[*it] = sz++;
		n = sz-1;
		f(i,0,b) {
			for(int x = mx[X[i*2]]; x < mx[X[i*2+1]]; x++)
				for(int y = my[Y[i*2]]; y < my[Y[i*2+1]]; y++)
					a[x][y] = 1;
		}
		*/
		int res = 0;
		fd(x,m-1,0) if (a[x][0] == 0) {
			a[x][0] = J;
			if (dfs(x,0,0)) res++;
			J++;
		}
//		f(i,0,m) f(j,0,n) printf("%d%c", a[i][j], j+1==n?10:32);

		printf("Case #%d: %d\n", ++caso, res);
	}
}


