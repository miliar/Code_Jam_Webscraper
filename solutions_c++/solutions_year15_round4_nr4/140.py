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


ll mod = 1e9 + 7;
ll modpow(ll a, ll pot) {
	ll res = 1;
	for (; pot; pot >>= 1) {
		if (pot&1) res = res * a % mod;
		a = a * a % mod;
	}
	return res;
}
ll inv[13];

int tc,caso;
ll b[105][12];
int dx[] = {1,2,2,3};
int dy[] = {1,3,6,4};

int main()
{
	f(i,1,12) inv[i] = modpow(i, mod-2);
	cin >> tc;
	while(tc--)
	{
		int r,c;
		cin >> r >> c;
		clr(b,0);
		b[0][1] ++;
		f(k,0,4) if (c % dy[k] == 0)
		{
			b[dx[k]][ dy[k] ] += dy[k];
		}
		f(i,0,r+1)
		{
			f(j,1,13)
			{
				b[i][j] %= mod;
				f(k,0,4) if (c%dy[k] == 0)
				{
					int i2 = i + dx[k] + 2, j2 = dy[k]*j/__gcd(dy[k], j);
					if (i2 > r) continue;
					b[i2][j2] += b[i][j] * dy[k] % mod;
//					if (i2 == r) cout << i << j << endl;
				}
			}
		}
		ll ans = 0;
//		adebug(b[r], 13);
		f(j,1,13) ans += b[r][j] * inv[j] % mod + b[r-2][j] * inv[j] % mod;
		ans %= mod;


//		f(i,2,r+1) a[i] = (b[i] + b[i-2]) % mod;
		printf("Case #%d: ", ++caso);
		printf("%lld\n", ans);
	}
}

