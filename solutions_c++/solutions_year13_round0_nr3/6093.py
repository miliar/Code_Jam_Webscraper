
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>

#define N 1010

using namespace std;

typedef unsigned long long ll;

int p[N];
int s[N];
int r[N];

int ispal(ll x)
{
	std::vector<int> d;
	while (x) {
		d.push_back(x % 10);
		x /= 10;
	}
	int pal = 1;
	int sz = d.size();
	int m = sz >> 1;
	for (int i = 0; i < m && pal; ++i)
		pal &= d[i] == d[sz - i - 1];
	return pal;
}

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);

	for (int i = 1; i < N; ++i)
		p[i] = ispal(i);

	memset(s, 0, sizeof s);
	for (int i = 1; i < N; ++i) {
		if (!p[i])
			continue;
		int j = i*i;
		if (j < N) {
			s[j] = p[j];
		}
	}

	r[1] = 1;
	for (int i = 2; i < N; ++i) {
		r[i] = r[i - 1];
		if (s[i])
			r[i]++;
	}

	for (int k = 1; k <= t; ++k) {
		ll a, b;
		scanf("%llu %llu", &a, &b);
		if (b == 1)
			printf("Case #%d: %d\n", k, 1);
		printf("Case #%d: %d\n", k, r[b] - r[a] + (r[a] > r[a - 1] ? 1 : 0));
	}
	return 0;
}
