#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define Fit(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define inf 1000000005
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
#define mod 1000000007
#define sz(a) ((int)(a).size())

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcount(s);}
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define Repd(i,n) for(int i = (n)-1; i >= 0; --i)
#define For(i,a,b) for(int i = (a); i <= (b); ++i)
#define Ford(i,a,b) for(int i = (a); i >= (b); --i)

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
#define eps 1e-9
typedef pair<int, int> II;
template<class T> T gcd(T a, T b){ T r; while (b != 0) { r = a % b; a = b; b = r; } return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
#define PI 2 * acos(0)

#define maxn 1000005

int f[maxn * 16], g[maxn * 16];
int test;
int n, d, vao[maxn], ra[maxn], a[maxn], number;
vector<int> V[maxn + maxn], VV[maxn + maxn];
int ret = 0;

void go(int u){
	vao[u] = ++number;
	Rep(i, sz(V[u])){
		go(V[u][i]);
	}
	ra[u] = ++number;
}

void add(int id, int l, int r, int u, int v, bool have){
	if(r < u || l > v) return;
	if(l >= u && r <= v){
		if(!f[id] && !have) ret += (r - l + 1) - g[id];
		f[id]++;
		return;
	}
	int mid = (l + r) >> 1;

	add(id + id, l, mid, u, v, have | (f[id] != 0));
	add(id + id + 1, mid + 1, r, u, v, have | (f[id] != 0));
	int A = g[id + id];
	if(f[id + id]) A = mid - l + 1;
	int B = g[id + id + 1];
	if(f[id + id + 1]) B = r - mid;
	g[id] = A + B;
}

void sub(int id, int l, int r, int u, int v, bool have){
	if(r < u || l > v) return;
	if(l >= u && r <= v){
		if(f[id] == 1 && !have) ret -= (r - l + 1) - g[id];
		f[id]--;
		return;
	}
	int mid = (l + r) >> 1;
	sub(id + id, l, mid, u, v, have | (f[id] != 0));
	sub(id + id + 1, mid + 1, r, u, v, have | (f[id] != 0));
	int A = g[id + id];
	if(f[id + id]) A = mid - l + 1;
	int B = g[id + id + 1];
	if(f[id + id + 1]) B = r - mid;

	g[id] = A + B;
}


void solve(int itest){

	Rep(i, maxn){
		V[i].clear();
		VV[i].clear();
	}
	ms(f, 0); ms(g, 0);

	cin >> n >> d;
	ll u1, u2, u3, u4;
	cin >> u1 >> u2 >> u3 >> u4;
	a[0] = u1;
	For(i, 1, n - 1){
		a[i] = (a[i - 1] * u2 + u3) % u4;
	}

	cin >> u1 >> u2 >> u3 >> u4;
	For(i, 1, n - 1){
		u1 = (u1 * u2 + u3) % u4;
		V[u1 % i].pb(i);
	}
	number = 0;
	ret = 0;
	go(0);
	Rep(i, n){
		VV[a[i]].pb(i);
	}

//	cout << a[0] <<  " " << a[1] << endl;
//	cout << V[0][0] << " " << V[0][1] << endl;
//	cout << a[V[0][0]] << " " << a[V[0][1]] << endl;

	Rep(i, n){
		if(a[i] < a[0] - d || a[i] > a[0]) {
//			cout << i << " " << vao[i] << " " << ra[i] << endl;
			add(1, 1, n + n, vao[i], ra[i], 0);
		}
	}
	if(a[0] < d){
		for(int i = a[0] + 1; i <= d; i++){
			Rep(j, sz(VV[i])){
				int u = VV[i][j];
				sub(1, 1, n + n, vao[u], ra[u], 0);
			}
		}
	}

//	cout << ret << endl;
	int res = ret;

	for(int gt = max(0, a[0] - d); gt < a[0]; gt++){
		Rep(i, sz(VV[gt])){
			int u = VV[gt][i];
			add(1, 1, n + n, vao[u], ra[u], 0);
		}

		Rep(i, sz(VV[gt + d + 1])){
			int u = VV[gt + d + 1][i];
			sub(1, 1, n + n, vao[u], ra[u], 0);
		}
		res = min(res, ret);
	}

	cout << "Case #" << itest << ": " << n - (res >> 1) << "\n";
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
    cin >> test;

    For(itest, 1, test){
    	solve(itest);
    }

    return 0;
}
