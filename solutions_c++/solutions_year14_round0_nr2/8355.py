#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define Fit(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define inf 1000000005
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
#define maxn (1 << 20) + 5
#define mod 1000000007

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return s == 0 ? 0 : cntbit(s >> 1) + (s & 1);}

typedef unsigned long long ull;
typedef long long ll;

typedef long double ld;

int test;
ld c, f, x;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	for(int itest = 1; itest <= test; itest++){
		cin >> c >> f >> x;
		ld res = 1000000000, T = 0, v = 2;
		for(int i = 0; i < x * f + 2; i++){
			res = min(res, x / v + T);
			T += c / v;
			v += f;
		}
		cout << fixed << setprecision(7);
		cout << "Case #" << itest << ": " << res << endl;
	}
}
