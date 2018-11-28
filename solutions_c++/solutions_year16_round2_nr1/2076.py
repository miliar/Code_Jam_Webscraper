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

int a[40], num[30];
string s;

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	int T, tc = 0;
	cin >> T;
	while (T--) {
		cin >> s;
		for (int i=0; i<30; i++) a[i] = 0;
		for (int i=0; i<sz(s); i++) {
			a[s[i] - 'A']++;
		}
//		cout << a['O' - 'A'] << endl;
		num[0] = min(a['Z' - 'A'], min(a['E' - 'A'], min(a['R' - 'A'], a['O' - 'A'])));
		a['Z' - 'A'] -= num[0];
		a['E' - 'A'] -= num[0];
		a['R' - 'A'] -= num[0];
		a['O' - 'A'] -= num[0];
		num[2] = min(a['T' - 'A'], min(a['W' - 'A'], a['O' - 'A']));
		a['T' - 'A'] -= num[2];
		a['W' - 'A'] -= num[2];
		a['O' - 'A'] -= num[2];
		num[6] = min(a['S' - 'A'], min(a['I' - 'A'], a['X' - 'A']));
		a['S' - 'A'] -= num[6];
		a['I' - 'A'] -= num[6];
		a['X' - 'A'] -= num[6];
		num[4] = min(a['F' - 'A'], min(a['O' - 'A'], min(a['U' - 'A'], a['R' - 'A'])));
		a['F' - 'A'] -= num[4];
		a['O' - 'A'] -= num[4];
		a['U' - 'A'] -= num[4];
		a['R' - 'A'] -= num[4];
		num[5] = min(a['F' - 'A'], min(a['I' - 'A'], min(a['V' - 'A'], a['E' - 'A'])));
		a['F' - 'A'] -= num[5];
		a['I' - 'A'] -= num[5];
		a['V' - 'A'] -= num[5];
		a['E' - 'A'] -= num[5];
		num[7] = min(a['S' - 'A'], min(a['E' - 'A'] / 2, min(a['V' - 'A'], a['N' - 'A'])));
		a['S' - 'A'] -= num[7];
		a['E' - 'A'] -= num[7] * 2;
		a['V' - 'A'] -= num[7];
		a['N' - 'A'] -= num[7];
		num[8] = min(a['E' - 'A'], min(a['I' - 'A'], min(a['G' - 'A'], min(a['H' - 'A'], a['T' - 'A']))));
		a['E' - 'A'] -= num[8];
		a['I' - 'A'] -= num[8];
		a['G' - 'A'] -= num[8];
		a['H' - 'A'] -= num[8];
		a['T' - 'A'] -= num[8];
		num[9] = min(a['N' - 'A'] / 2, min(a['I' - 'A'], a['E' - 'A']));
		a['N' - 'A'] -= num[9] * 2;
		a['I' - 'A'] -= num[9];
		a['E' - 'A'] -= num[9];
		num[1] = min(a['O' - 'A'], min(a['N' - 'A'], a['E' - 'A']));
		a['O' - 'A'] -= num[1];
		a['N' - 'A'] -= num[1];
		a['E' - 'A'] -= num[1];
		num[3] = min(a['T' - 'A'], min(a['H' - 'A'], min(a['R' - 'A'], a['E' - 'A'] / 2)));
//		cout << num[1] << endl;
		cout << "Case #" << ++tc << ": ";
		for (int i=0; i<=9; i++) {
			for (int j=1; j<=num[i]; j++) cout << i;
		}
		cout << endl;
	}


}

