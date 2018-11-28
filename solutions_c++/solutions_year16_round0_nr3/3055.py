//#pragma comment(linker, "/STACK:134217728")
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define MOD 1000000009
#define INF 1000000007
#define y1 agaga
#define ll long long
#define ull unsigned long long

bool prime(long long x) {
	if (x < 2) return false;
	if (x % 2 == 0) return false;
	long long i = 3;
	while (i*i <= x) {
		if (x % i == 0)
			return false;
		i += 2;
	}
	return true;	
}

string toB(int x, int len) {
	string s = "";
	RFOR(i, len, 0) {
		if ((x >> i) & 1) {
			s += '1';
		}
		else {
			s += '0';
		}
	}
	return s;
}

bool good(int x, int len) {
	FOR(base, 2, 11) {
		long long sum = 0;
		long long factor = 1;
		FOR(i, 0, len) {
			if ((x >> i) & 1) {
				sum += factor;
			}
			factor *= base;
		}
		//cout << " base = " << base << " sum = " << sum << endl;
		if (prime(sum)) return false;
	}
	return true;
}

long long least_div(long long x) {
	long long i = 2;
	while (i*i <= x) {
		if (x % i == 0) {
			return i;
		}
		++i;
	}
	throw - 1;
}

void g(int x, int len) {
	FOR(base, 2, 11) {
		long long sum = 0;
		long long factor = 1;
		FOR(i, 0, len) {
			if ((x >> i) & 1) {
				sum += factor;
			}
			factor *= base;
		}		
		cout << " " << least_div(sum);
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	FOR(T, 0, t) {
		cout << "Case #" << T + 1 << ":" << endl;
		int n;
		int k;
		cin >> n >> k;

		FOR(mask, 0, 1 << (n - 2)) {
			int real = (mask<<1) + (1 << (n - 1)) + 1;
			if (good(real, n)) {
				cout << toB(real, n);
				g(real,n);
				cout << endl;
				--k;
				if (k == 0) {
					return 0;
				}
			}
		}


	}

	return 0;
}