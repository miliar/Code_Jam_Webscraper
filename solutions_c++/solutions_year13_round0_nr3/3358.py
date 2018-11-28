#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>

using namespace std;


long long mas[] = {  1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004 };


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
 
	long long t, a, b, posa = 0, posb = 0, ans = 0;

	bool oka = false, okb = false;

	int i, j;

	cin >> t;

	for (i = 0; i < t; i++)
	{
		cin >> a >> b;

		for (j = 0; j < 39 && (!oka || !okb); j++)
		{
			if ( !oka && mas[j] >= a ) { posa = j; oka = true; }
			if ( !okb && mas[j] > b ) { posb = j; okb = true; }
		}

		oka = false;
		okb = false;

		ans = posb - posa;

		printf("Case #%d: ", i + 1);
		printf("%d\n", ans);
	}


 
	return 0;
}
