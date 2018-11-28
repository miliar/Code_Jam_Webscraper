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




int main() {
	input_txt;

	int t;
	cin >> t;
	for (int ii = 0; ii < t; ++ii) {
		string a, b;
		cin >> a >> b;
		reverse(all(a));
		reverse(all(b));

		int dig_1[3];
		int dig_2[3];

		pair<int, int> best = mp(-999999, 999999);
		int best_diff = 99999999;

		for (int i1 = 0; i1 < 10; ++i1) {
			for (int i2 = 0; i2 < 10; ++i2) {
				for (int i3 = 0; i3 < 10; ++i3) {
					for (int j1 = 0; j1 < 10; ++j1) {
						for (int j2 = 0; j2 < 10; ++j2) {
							for (int j3 = 0; j3 < 10; ++j3) {
								dig_1[0] = i1;
								dig_1[1] = i2;
								dig_1[2] = i3;
								dig_2[0] = j1;
								dig_2[1] = j2;
								dig_2[2] = j3;

								int aa = 0;
								int mul = 1;
								for (int i = 0; i < a.size(); ++i) {
									if (a[i] == '?') {
										aa += mul * dig_1[i];
									}
									else {
										aa += mul * (a[i] - '0');
									}
									mul *= 10;
								}

								mul = 1;
								int bb = 0;
								for (int i = 0; i < b.size(); ++i) {
									if (b[i] == '?') {
										bb += mul * dig_2[i];
									}
									else {
										bb += mul * (b[i] - '0');
									}
									mul *= 10;
								}

								int my_diff = abs(aa - bb);
								if (my_diff < best_diff) {
									best_diff = my_diff;
									best = mp(aa, bb);
								}
								else if (my_diff == best_diff && mp(aa, bb) < best) {
									best_diff = my_diff;
									best = mp(aa, bb);
								}

							}
						}
					}
				}
			}
		}
		printf("Case #%d: ", ii + 1);

		string aaa;
		while (best.first) {
			aaa.push_back(best.first % 10 + '0');
			best.first /= 10;
		}
		string bbb;
		while (best.second) {
			bbb.push_back(best.second % 10 + '0');
			best.second /= 10;
		}

		while (aaa.size() < a.size())aaa.push_back('0');
		while (bbb.size() < b.size())bbb.push_back('0');
		reverse(all(aaa));
		reverse(all(bbb));
		cout << aaa << " " << bbb << endl;
	}


	//time_elapsed();
	return 0;
}