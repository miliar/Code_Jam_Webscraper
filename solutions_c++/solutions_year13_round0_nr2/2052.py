#include <cstdio>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ctime>

#include <iostream>
#include <fstream>
#include <sstream>

#include <algorithm>
#include <utility>

#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <list>

using namespace std;

#define fi(i, n) for (int i = 0; i < (n); ++i)
#define fv(i, v) fi (i, (v).size())
#define fab(i, a, b) for (int i = (a); i <= (b); ++i)
#define fba(i, b, a) for (int i = (b); i >= (a); --i)

#define V vector
#define VI vector<int>
#define VS vector<string>
#define uint unsigned int
#define uchar unsigned char
#define LL long long
#define uLL unsigned LL

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz size()

uLL fact(int n, uLL mod) { return n ? n * fact(n - 1, mod) % mod : 1; }
uLL gcd(uLL a, uLL b) { return a ? gcd(b % a, b) : b; }
uLL qpow(uLL a, uLL b, uLL mod) { if (!b) return 1; if (b % 2) return a * qpow(a, b - 1, mod) % mod; else {uLL t = qpow(a, b / 2, mod); return t * t % mod; }}

void solve_the_problem() {
	int a[100][100];
	int h[100], v[100];
	memset(h, 0, 100 * sizeof(int));
	memset(v, 0, 100 * sizeof(int));
	int m, n;
	cin >> n >> m;
	fi(i, n) {
		fi(j, m) {
			cin >> a[i][j];
			h[i] = max(h[i], a[i][j]);
			v[j] = max(v[j], a[i][j]);
		}
	}
	fi(i, n) {
		fi(j, m) {
			if (a[i][j] < h[i] && a[i][j] < v[j]) {
				cout << "NO";
				return;
			}
		}
	}
	cout << "YES";
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	fab(i, 1, t) {
		cerr << "Test #" << i << ":" << endl;
		cout << "Case #" << i << ": ";
		solve_the_problem();
		cout << endl;
	}
	return 0;
}
