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

string s;
pii r[1040];

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	int T, tc = 0;
	cin >> T;
	while (T--) {
		cin >> s;
		int F = -1;
		for (int i=0; i<sz(s); i++) r[i] = mp(0, i);
		for (int i=0; i<sz(s); i++) {
			int x = s[i] - 'A';
//			cout << x << " " << s[F] - 'A' << " " << s[F] << endl;
			if (F == -1 || x >= s[F] - 'A') {
//				cout << F << endl;
				for (int j=0; j<i; j++) r[j].FI++;
				r[i].FI = 0;
				F = i;
			}
			else {
				r[i].FI = i;
			}
		}
		
		sort(r, r + sz(s));
		cout << "Case #" << ++tc << ": ";
		for (int j=0; j<sz(s); j++) printf("%c", s[r[j].SE]);
		cout << endl;
	}


}

