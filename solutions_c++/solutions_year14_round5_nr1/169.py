#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

const int N = 1000000 + 10;

int n;
long long p, q, r, ss;
long long a[N];
long long s[N];
long long f[N];

void solve(int test)
{
	printf("Case #%d: ", test);
	cin >> n >> p >> q >> r >> ss;
	if (n == 1) {
		printf("%.16f\n", 0.0);
		return;
	}
	long long sum = 0;
	for(int i = 0; i < n; ++ i) {
		a[i] = (i * p + q) % r + ss;
		sum += a[i];
		s[i] = sum;
	}
	if (s[n - 1] == 0) {
		printf("%.16f\n", 0.0);
		return;
	}
	long long ret = max(s[0], s[n - 1] - s[0]);
	f[0] = s[0];
	int ptr = 0;
	for(int i = 1; i < n; ++ i) {
		while (ptr < i && max(s[ptr], s[i] - s[ptr]) > max(s[ptr + 1], s[i] - s[ptr + 1]))
			++ ptr;
		f[i] = max(s[ptr], s[i] - s[ptr]);
		ret = min(ret, max(s[n - 1] - s[i], f[i]));
	}
	double tmp = s[n - 1] - ret;
	tmp /= s[n - 1];
	printf("%.16f\n", tmp);
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int testcase;
	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) 
		solve(i);
	fclose(stdout);
	return 0;
}
