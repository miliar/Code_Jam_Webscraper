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
//#define mod 1000000000
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

#define maxn 400005

typedef pair<ld, ld> DD;

vector<DD> V1, V2;
ld V, X;
int n, test;

bool thoaman(ld d){
	if(!sz(V1)){
		ld RR = 0;
		Rep(i, sz(V2)) if(V2[i].fi < eps) RR += V2[i].se * d;
		if(RR >= V) return true;
		return false;
	}
	ld VV = 0, TT = 0;
	Rep(i, sz(V1)){
		VV += V1[i].se * d;
		TT += V1[i].se * (V1[i].fi) * d;
	}

	bool ok = false;
	if(TT < eps && VV >= V) return true;
	Rep(i, sz(V2)){
		ld RR = V2[i].se * d;
		if(RR * V2[i].fi >= TT){
			ok = true;
			VV += TT / V2[i].fi;
			break;
		} else{
			VV += RR;
			TT -= RR * V2[i].fi;
		}
	}

	if(ok && VV >= V) return true;

	VV = 0; TT = 0;
	Rep(i, sz(V2)){
		VV += V2[i].se * d;
		TT += V2[i].se * (V2[i].fi) * d;
	}


	if(TT < eps && VV >= V) return true;
	ok = false;
	Rep(i, sz(V1)){
		ld RR = V1[i].se * d;
		if(RR * V1[i].fi >= TT){
			ok = true;
			VV += TT / V1[i].fi;
			break;
		} else{
			VV += RR;
			TT -= RR * V1[i].fi;
		}
	}
	if(ok && VV >= V) return true;

	return false;
}

void solve(int itest){

	cout << fixed << setprecision(9);
	cout << "Case #" << itest << ": ";
	cin >> n >> V >> X;

	ld u, v;
	V1.clear(); V2.clear();
	Rep(run, n){
		cin >> u >> v;
		if(v >= X - eps) V2.pb(mp(v - X, u));
		else V1.pb(mp(X - v, u));
	}
	sort(all(V1));
	sort(all(V2));

	ld l = 0, r = inf, mid;
	Rep(run, 200){
		mid = (l + r) / 2;
		if(thoaman(mid)){
			r = mid;
		} else l = mid;
	}

	if(l >= inf - 100){
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	cout << l << endl;
}

int main(){

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> test;
    For(itest, 1, test){
    	solve(itest);
    }

    return 0;
}
