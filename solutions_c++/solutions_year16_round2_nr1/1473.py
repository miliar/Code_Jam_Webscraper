#pragma comment(linker, "/STACK:134217728") //128mb
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cassert>
#include <climits>
#include <ctime>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <random>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <complex>
using namespace std;


#define input_txt freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout)
#define in_out(x) freopen(x".in", "r", stdin);freopen(x".out", "w", stdout)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(s) int((s).size())
#define all(x) x.begin(),x.end()

typedef long long ll;
typedef long long llong;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef complex<double> comp;

const long long MOD = 1000000000 + 7; //1e9+7
const long long MAXN = 100000 + 100; //1e5
const long long MAGIC = 123123123;
const double PI = 4 * atan(1.);
const double EPS = 1E-7;



struct cmp_for_set {
	bool operator()(const int & a, const int & b) { return a > b; }
};

void time_elapsed() { cout << "\nTIME ELAPSED: " << (double)clock() / CLOCKS_PER_SEC << " sec\n"; }
#define DOUT_VAR(x) cout << #x << " = " << (x) << endl
template<typename T> void DOUT_VEC(vector<T> & vec) { puts("");  for (auto i : vec) cout << i << " "; puts(""); }
template<typename T> void DOUT_TABLE(vector<vector<T>> & vec) { puts(""); for (auto i : vec) { for (auto j : i) cout << j << " "; cout << endl; }puts(""); }

template<typename T> T gcd(T a, T b) { return ((!b) ? a : gcd(b, a%b)); }
template<typename T>T gcd(T a, T b, T&x, T&y) { if (!a) { x = 0, y = 1; return b; }T x1, y1; T d = gcd(b%a, a, x1, y1); x = y1 - (b / a)*x1; y = x1; return d; }

template<typename T> T lcm(T a, T b) { return (a / gcd(a, b))*b; }
template<typename T, typename M> T neg_mod(T a, M mod) { return ((a%mod) + mod) % mod; }
ll binpow(ll x, ll p) { ll res = 1; while (p) { if (p & 1) res *= x; x *= x; p >>= 1; }return res; }
ll binpow_mod(ll x, ll p, ll m) { ll res  = 1; while (p) { if (p & 1) res = (res*x) % m; x = (x*x) % m; p >>= 1; }return res; }

string sign[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};


string solve(vector<int> cnt) {
	vector<int>res(10);
	res[0] = cnt['Z' - 'A'];
	for (int i = 0; i < sign[0].size(); ++i) {
		cnt[sign[0][i] - 'A'] -= res[0];
	}

	res[2] = cnt['W' - 'A'];
	for (int i = 0; i < sign[2].size(); ++i) {
		cnt[sign[2][i] - 'A'] -= res[2];
	}

	res[4] = cnt['U' - 'A'];
	for (int i = 0; i < sign[4].size(); ++i) {
		cnt[sign[4][i] - 'A'] -= res[4];
	}

	res[6] = cnt['X' - 'A'];
	for (int i = 0; i < sign[6].size(); ++i) {
		cnt[sign[6][i] - 'A'] -= res[6];
	}

	res[8] = cnt['G' - 'A'];
	for (int i = 0; i < sign[8].size(); ++i) {
		cnt[sign[8][i] - 'A'] -= res[8];
	}

	for (int i = 1; i < 9; i += 2) {
		res[i] = cnt[sign[i][0] - 'A'];
		for (int j = 0; j < sign[i].size(); ++j) {
			cnt[sign[i][j] - 'A'] -= res[i];
		}
	}
	res[9] = cnt['N' - 'A'] / 2;

	string ans;
	for (int i = 0; i < 10; ++i) {
		for (int j = 0; j < res[i]; ++j) {
			ans.push_back('0' + i);
		}
	}
	return ans;
}

// zero - z
// two - w
// four - u
// six - x
// eight - g

//rest - 5 digits:
// one, three, five, seven, nine

// one - o
// three - t
// five - f
// seven - s

//nine - n

string toletters(const string & s) {
	string res;
	for (int i = 0; i < s.size(); ++i) {
		res += sign[s[i] - '0'];
	}
	return res;
}

int main() {
	input_txt;


	int n;
	cin >> n;
	int t = 1;
	for (int i = 0; i < n; ++i) {
		string str;
		cin >> str;
		printf("Case #%d: ", t++);
		vector<int>cnt(26);
		for (int j = 0; j < str.size(); ++j) {
			cnt[str[j] - 'A']++;
		}
		cout << solve(cnt) << endl;

		string chk = toletters(solve(cnt));
		sort(all(chk));
		sort(all(str));
		assert(chk == str);
	}


	//time_elapsed();
	return 0;
}