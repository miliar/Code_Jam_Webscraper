#pragma comment (linker, "/STACK:128000000")
#include <iostream> 
#include <cstdio> 
#include <fstream>
#include <functional>
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <stack> 
#include <cmath> 
#include <algorithm> 
#include <cstring> 
#include <bitset> 
#include <ctime> 
#include <sstream>
#include <stack> 
#include <cassert> 
#include <list> 
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();
void prec();

//int timer = 0;
#define FILENAME ""

int main() {
	string s = FILENAME;
#ifdef YA
	//assert(!s.empty());
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//cerr<<FILENAME<<endl;
	//assert (s != "change me please");
	clock_t start = clock();
#else
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	//freopen(FILENAME ".in", "r", stdin);
	//freopen(FILENAME ".out", "w", stdout); 
	cin.tie(0);
#endif
	cout.sync_with_stdio(0);
	cout.precision(10);
	cout << fixed;
	int t = 1;

	prec();

	cin >> t;
	
	for (int i = 1; i <= t; ++i) {
		//++timer;
		cout << "Case #" << i << ":\n";
		solve();
	}
#ifdef YA
	cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
	return 0;
}

vector <int> primes;

void prec() {
	int N = 1000;
	for (int i = 2; i < N; ++i) {
		bool f = false;
		for (int j : primes) {
			if (i % j == 0) {
				f = true;
				break;
			}
		}
		if (!f) {
			primes.push_back(i);
		}
	}
}

#define int li

void solve() {
	int N, J;
	cin >> N >> J;

	vector <int> repr(N);
	repr[0] = repr[N - 1] = 1;

	vector <int> divisors(11);

	for (int i = 0; J && i < (1 << (N - 2)); ++i) {
		
		bool ok = true;
		for (int j = 0; j < N - 2; ++j) {
			if ((1 << j) & i) {
				repr[j + 1] = 1;
			}
			else {
				repr[j + 1] = 0;
			}
		}

		for (int base = 2; base <= 10; ++base) {
			int num = 0;
			for (int j = N - 1; j >= 0; --j) {
				num = num * base + repr[j];
			}
			int found = false;
			for (int t : primes) {
				if (num % t == 0) {
					found = true;
					divisors[base] = t; 
					break;
				}
			}
			if (!found) {
				ok = false;
				break;
			}
		}

		if (ok) {
			--J;
			cerr << J << endl;
			for (int j = N - 1; j >= 0; --j) {
				cout << repr[j];
			}
			for (int j = 2; j <= 10; ++j) {
				cout << " " << divisors[j];
			}
			cout << "\n";
		}
	}
}