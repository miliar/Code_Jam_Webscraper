#include <cstdio>
#include <iostream>

using namespace std;

long long a[42] = {0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll,100000020000001ll};

int ttt;

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	scanf("%d", &ttt);
	for (int it = 1; it <= ttt; it++)
	{
		printf("Case #%d: ", it);
		int ans = 0;
		long long l, r;
		cin >> l >> r;
		for (int i = 1; i <= 40; i++)
			if (a[i] >= l && a[i] <= r) ans++;
		printf("%d\n", ans);
	}
	return 0;
}