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

struct seg{
	int l, r;
	seg(){};
	seg(int _l, int _r){
		l = _l; r = _r;
	}
	bool operator <(const seg &S)const{
		return l + r > S.l + S.r;
	}
};

int a[1005], n, k, d[1005];
bool f[105][105];
seg A[1005];
int test;

void solve(int itest){

	cin >> n >> k;
	ms(d, 0);
	For(i, 1, n - k + 1) cin >> a[i];
	For(i, 1, k) A[i] = seg(0, 0);
	ms(f, 0);

	For(i, 1, n - k){
		int u = (i - 1) % k + 1;
		d[u] += a[i + 1] - a[i];
		if(d[u] >= 0) A[u].r = max(A[u].r, d[u]);
		else A[u].l = max(A[u].l, -d[u]);
	}

	sort(A + 1,A  + k + 1);
	f[1][A[1].l % k] = 1;
	for(int i = 2; i <= k; i++) for(int t = 0; t < k; t++) if(f[i - 1][t]){
		for(int j = 0; j <= k && j + A[i].l + A[i].r <= A[1].l + A[1].r; j++){
			f[i][(t + j + A[i].l) % k] = 1;
		}
	}

	int res = A[1].l + A[1].r;
	if(!f[k][((a[1] % k) + k) % k]) res++;

	cout << "Case #" << itest << ": " << res << "\n";
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

//    cout << clock() << endl;

    return 0;
}
