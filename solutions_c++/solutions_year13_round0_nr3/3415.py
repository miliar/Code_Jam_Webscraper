#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[10];

bool ispal(int x)
{
	int sz = 0;
	while (x) {
		a[sz++] = x%10;
		x /= 10;
	}
	for (int i = 0; 2*i < sz; ++i)
		if (a[i] != a[sz-i-1]) return false;
	return true; 
}

int solve(int A, int B)
{
	int cnt = 0;
	for (int i = 1; i*i <= B; ++i) {
		if (i*i >= A)
			cnt += ispal(i) & ispal(i*i);
	}
	return cnt;
}

int main()
{
	freopen("input", "r", stdin);

	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; ++t) {
		int A, B;
		scanf("%d %d\n", &A, &B);
		printf("Case #%d: %d\n", t, solve(A, B));
	}

	return 0;
}
