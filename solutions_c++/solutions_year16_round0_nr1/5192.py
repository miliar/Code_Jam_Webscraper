//This is getting accepted!
#include<bits/stdc++.h>

using namespace std;

#define FI first
#define SE second
#define pb push_back
#define mp make_pair
#define ll long long
#define sz(a) ((int)(a).size())
#define __builtin_popcount __builtin_popcounll

typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<int, pii> ppi;

const double PI = acos(0) * 2;
const double EPS = 1e-8;
const ll MOD = 1e9 + 7;
const int MAXN = 1e5 + 5;
const int oo = 1e9;
const double foo = 1e30;

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcounll(s);}

int T, a[10];
ll n;

int check() {
	for (int i=0; i<10; i++) if (a[i] == 0) return 0;
	return 1;
}

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	int tc;
	cin >> T;
	while (T--) {
		cin >> n;
		if (n == 0) cout << "Case #" << ++tc << ": "<<  "INSOMNIA" << endl;
		else {
			ll j = 0;
			for (int i=0; i<10; i++) a[i] = 0;
			while (!check()) {
				j++;
				ll N = n * j;
				while (N != 0) {
					a[N % 10] = 1;
					N /= 10;
				}
			}
			cout << "Case #" << ++tc << ": " << j * n << endl;
		}
	}


}

