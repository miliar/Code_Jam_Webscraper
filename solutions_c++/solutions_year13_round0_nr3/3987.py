#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
char s[20], t[20];
bool check(long long x)
{
	sprintf(s, "%lld", x);
	int n = strlen(s);
	strcpy(t, s);
	reverse(t, t + n);
	return !strcmp(s, t);
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	vector <long long> ans;
	for (int i = 1; i <= 10000000; ++ i)
		if (check(i) && check((long long) i * i))
			ans.push_back(i);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++ cas)
	{
		long long l, r;
		scanf("%lld%lld", &l, &r);
		int tot = 0;
		for (int i = 0; i < ans.size(); ++ i)
			if (l <= ans[i] * ans[i] && ans[i] * ans[i] <= r)
				++ tot;
		printf("Case #%d: %d\n", cas, tot);
	}
	return 0;
}
