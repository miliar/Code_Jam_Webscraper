#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

#define pb push_back
typedef long long LL;
const int MAXN = 10000000;

vector<LL> lis;

bool pla(LL a)
{
	int num[20], cnt = 0;
	for (; a; num[++cnt] = a % 10, a /= 10);
	for (int i = 1, j = cnt; i <= j; ++i, --j)
		if (num[i] != num[j])
			return false;
	return true;
}
int id;
void solve()
{
	LL l, r;
	cin >> l >> r;
	int CC = 0;
	for (int i = 0; i < (int)lis.size() && lis[i] <= r; ++i)
		if (lis[i] >= l && lis[i] <= r)
			++CC;
	printf("Case #%d: %d\n",id, CC);
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
#endif
	for (int i = 1; i <= MAXN; ++i)
		if (pla(i) && pla((LL)i * i))
			lis.pb((LL) i * i);
	int test;
	scanf("%d", &test);
	while (test)
		++id,
		solve(),
		--test;
	fclose(stdin);
	fclose(stdout);
	return 0;
}
