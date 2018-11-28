#include <vector>
#include <stdio.h>
#include <iostream>
#include <map>
#include <queue>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define sz(v) ((int)v.size())
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int N = (int)3e5;

int n, d[11];

int solve(int n) {
	for (int i = 0; i < 10; i++) d[i] = 0;
	for (int i = 1; i <= 100; i++) {
		int x =  n * i;
		while (x) {
			d[x % 10] = 1;
			x /= 10;
		}
		bool ok = true;
		for (int i = 0; i < 10; i++)
			if (!d[i]) ok = false;
		if (ok)
			return i * n;
	}
}

int main () {
	freopen("in0.in", "r", stdin);
	freopen("out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d", &n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", i);	
			continue;
		}
		printf("Case #%d: %d\n", i, solve(n));
	}
	

	return 0;
}

