#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
#define For(i,a,b) for(int i=a;i<=b;i++)
#define Ford(i,a,b) for(int i=a;i>=b;i--)
#define fi first
#define se second
#define sr(x) (int)x.size()
#define BUG(x) {cout << #x << " = " << x << endl;}
#define PR(x,a,b) {cout << #x << " = "; For(_,a,b) cout << x[_] << ' '; cout << endl;}
#define Bit(s,i) (((s)&(1<<(i)))>0)
#define Two(x) (1<<(x))
const int MOD = 1000000007;
const int nmax = 110;
const double E = 1e-8;
const double PI = acos(-1);
typedef long long LL;
typedef pair<int,int> pii;
int n,m,stest;

int a[nmax][nmax];
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};

bool inside(int i, int j) {
	return  1 <= i && i <= n && 1 <= j && j<=m;
}

bool check(int i, int j, int h) {
	i += dx[h];
	j += dy[h];
	while ( a[i][j] == -1 && inside(i,j) ) {
		i += dx[h];
		j += dy[h];
	}
	return inside(i,j);
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> stest;
	For(test,1,stest) {
		cin >> n >> m;
		For(i,1,n) For(j,1,m) {
			char ch;
			cin >> ch;
			if ( ch == '.' ) a[i][j] = -1;
			else if ( ch == 'v' ) a[i][j] = 0;
			else if ( ch == '>' ) a[i][j] = 1;
			else if ( ch == '^' ) a[i][j] = 2;
			else a[i][j] = 3;
		}
		int res = 0;
		bool noAns = false;
		For(i,1,n) For(j,1,m) {
			int h = a[i][j];
			if ( h == -1 ) continue; 
			if ( check(i,j,h) ) continue;
			bool Find = false;
			For(t,0,3) if ( check(i,j,t) ) {
				Find = true;
				break;
			}
			if (!Find) noAns = true;
			res++;
		}
		cout << "Case #" << test << ": ";
		if ( noAns ) cout << "IMPOSSIBLE"; else cout << res;
		cout << endl;
	}
	return 0;
}