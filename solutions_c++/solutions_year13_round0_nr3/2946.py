#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int ar[39] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001,
	102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201,
	12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
	1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};

int t;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long a, b;
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		cin >> a >> b;
		int res = 0;
		for (int i = 0; i < 39; i++)
		{
			res += (ar[i] >= a && ar[i] <= b);
		}
		printf("Case #%d: %d\n", q + 1, res);
	}
	return 0;
}