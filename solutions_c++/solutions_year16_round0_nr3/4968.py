#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("C-small-attempt1.out", "wt", stdout);
#endif
}

long long isNonPrime(long long n) {
	if (n <= 1) return 0;
	for (long long i = 2; i * i <= n; i++) {
		if (n % i == 0) return i;
	}
	return 0;
}

pair<long long, int> getBinary(int b) {
	char line[40] = {0};
	int len = 0;
	while (b) {
		line[len] = '0' + (b & 1);
		b >>= 1;
		len++;
	}
	for (int i = 0; i < len / 2; i++) {
		swap(line[i], line[len - 1 - i]);
	}
	long long r;
	sscanf(line, "%lld", &r);
	return make_pair(r, len);
}

long long inter(long long n, int b) {
	long long s = 0;
	long long m = 1;
	while (n > 0) {
		int d = (n % 10);
		s += m * d;
		m *= b;
		n /= 10;
	}
	return s;
}

long long dig[11];
bool allNonPrime(long long n) {
	for (int i = 2; i <= 10; i++) {
		long long k = isNonPrime(inter(n, i));
		if (!k) {
			return false;
		}
		dig[i] = k;
	}
	return true;
}

int MAXN = 16;
void interpret(long long n, long long J) {
	cout << endl;
	int f = 0;
	for (long long i = 3; i < (1 << MAXN) && f < J; i++) {
		pair<long long, int> p = getBinary(i);		
		long long b = p.first;
		if ((b & 1) == 0) continue;
		if (p.second != n) continue;
		if (allNonPrime(b)) {
			f++;
			cout << b;
			for (int j = 2; j <= 10; j++) {
				cout << " " << dig[j];
			}
			cout << endl;
		}
	}
}

void solve() {
	long long n, j;
	cin >> n >> j;
	interpret(n, j);
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
            printf("Case #%d: ", i + 1);
            solve();
    }
    return 0;
}
