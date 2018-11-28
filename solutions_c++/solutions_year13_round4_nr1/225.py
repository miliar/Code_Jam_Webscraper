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
#define pii pair<ll,ll>
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define eps (1e-9)
#define oo (1<<30)
#define SZ(a) (int)a.size()
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; f(i,0,m)f(j,0,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define N 1
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}

ll mod = 1000002013;
int tc, caso;
pii pila[2005]; int top = 0;
ll cua(int x) {
	return (ll)x * x % mod;
}
bool orden(pii a, pii b) {
	return a.fst < b.fst || (a.fst == b.fst && a.snd > b.snd);
}

int main(){
	cin >> tc;
	while(tc--) {
		int n,m;
		cin >> n >> m;
		vector<pii> P;
		ll ini = 0, fin = 0;
		f(i,0,m) {
			int o,e,p;
			scanf("%d%d%d", &o,&e, &p);
			P.pb(pii(o,p));
			P.pb(pii(e,-p));
			ini += cua(e-o) * p % mod;
		}
		sort(all(P), orden);
		top = 1;
		f(i,0,P.size()) {
//			debug(P[i].snd);
			if (P[i].snd > 0) {
				pila[top++] = P[i];
			} else {
				while(pila[top-1].snd + P[i].snd <= 0) {
					fin += cua(P[i].fst - pila[top-1].fst) * pila[top-1].snd % mod;
//					debug(i);
//					debug(top);
//					debug(P[i].fst);
//					debug(pila[top-1].fst);
					P[i].snd += pila[top-1].snd;
					top--;
					if (P[i].snd == 0) break;
				}
				pila[top-1].snd += P[i].snd;
				fin += cua(P[i].fst - pila[top-1].fst) * -P[i].snd % mod;
			}
		}
		printf("Case #%d: ", ++caso);
		ini %= mod;
		fin %= mod;
		ll res = fin - ini + mod;
		if (res&1) res += mod;
		res/=2;
		res %= mod;
//		debug(ini);
//		debug(fin);
		cout << res << endl;
	}
}

