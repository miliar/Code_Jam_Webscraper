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
int a[10005];
int vis[10005];

int main(){
	cin >> tc;
	while(tc--) {
		int n,x; cin >> n >> x;
		f(i,0,n) scanf("%d", a + i);
		f(i,0,n) vis[i] = 0;
		sort(a, a + n);
		int quedan = n;
		int pares = 0;
		int j = n-1;
		int res;
		f(i,0,n) {
			for (; j > i; j--) {
				if (vis[j]) continue;
				if (a[i] + a[j] <= x) break;
			}
			if (j == i) res = pares + quedan;
			else {
				pares++;
				quedan -= 2;
				vis[i] = vis[j] = 1;
			}
		}
		printf("Case #%d: %d\n", ++caso, res);
	}
}


