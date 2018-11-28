
#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <string.h>
#include <string>
#include <limits.h>
#include <algorithm>
#include <set>
#include <ctime>
using namespace std;
#define SZ(x) ((int)(x).size())
#define rep(i,a,n) for (int i=a; i<(int)n; i++)
#define per(i,n,a) for (int i=n; i>=a; i--)
#define hk push_back
#define pk pop_back
#define mp make_pair
#define PI 3.141592653589793
#define clr(a) memset(a, 0, sizeof(a))
#define clr1(a) memset(a, -1, sizeof(a))
typedef vector<int> VI;
typedef vector< pair<int, int> > VIP;
typedef vector< pair<int, pair<int, double> > > VIPP;
typedef vector<string> VS;
typedef vector <double> VD;
typedef vector <bool> VB;
typedef long long ll;
#define MAX_V 1000
const ll mod = 1000000007;
ll powmod(ll a, ll b) {
	ll res = 1; a %= mod; for (; b; b >>= 1){ if (b & 1)res = res*a%mod; a = a*a%mod; }return res;
}

int T;
string s;
int cnt[27], ans[10];

int main() {
	cin >> T;
	int T1 = 0;
	while (T1++ < T) {
		clr(cnt); clr(ans);
		cin >> s;


		rep(i, 0, s.length()) {
			cnt[s[i] - 'A']++;
		}
		ans[0] = cnt['Z' - 'A'];
		cnt['Z' - 'A'] -= ans[0];
		cnt['E' - 'A'] -= ans[0];
		cnt['R' - 'A'] -= ans[0];
		cnt['O' - 'A'] -= ans[0];

		ans[2] = cnt['W' - 'A'];
		cnt['T' - 'A'] -= ans[2];
		cnt['W' - 'A'] -= ans[2];
		cnt['O' - 'A'] -= ans[2];

		ans[4] = cnt['U' - 'A'];
		cnt['F' - 'A'] -= ans[4];
		cnt['O' - 'A'] -= ans[4];
		cnt['U' - 'A'] -= ans[4];
		cnt['R' - 'A'] -= ans[4];

		ans[8] = cnt['G' - 'A'];
		cnt['E' - 'A'] -= ans[8];
		cnt['I' - 'A'] -= ans[8];
		cnt['G' - 'A'] -= ans[8];
		cnt['H' - 'A'] -= ans[8];
		cnt['T' - 'A'] -= ans[8];

		ans[5] = cnt['F' - 'A'];
		cnt['F' - 'A'] -= ans[5];
		cnt['I' - 'A'] -= ans[5];
		cnt['V' - 'A'] -= ans[5];
		cnt['E' - 'A'] -= ans[5];

		ans[3] = cnt['T' - 'A'];
		cnt['T' - 'A'] -= ans[3];
		cnt['H' - 'A'] -= ans[3];
		cnt['R' - 'A'] -= ans[3];
		cnt['E' - 'A'] -= ans[3];
		cnt['E' - 'A'] -= ans[3];

		ans[1] = cnt['O' - 'A'];
		cnt['O' - 'A'] -= ans[1];
		cnt['N' - 'A'] -= ans[1];
		cnt['E' - 'A'] -= ans[1];

		ans[6] = cnt['X' - 'A'];
		cnt['S' - 'A'] -= ans[6];
		cnt['I' - 'A'] -= ans[6];
		cnt['X' - 'A'] -= ans[6];

		ans[7] = cnt['S' - 'A'];
		cnt['S' - 'A'] -= ans[7];
		cnt['E' - 'A'] -= ans[7];
		cnt['V' - 'A'] -= ans[7];
		cnt['E' - 'A'] -= ans[7];
		cnt['N' - 'A'] -= ans[7];

		ans[9] = cnt['I' - 'A'];

		cout << "Case #" << T1 << ": ";
		rep(i, 0, 10) {
			while (ans[i]) {
				cout << i;
				ans[i]--;
			}
		}
		cout << endl;
	}

	return 0;
}