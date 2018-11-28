#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>

using namespace std;

#define ll long long
#define vt vector
#define inf 1000000000
#define mod 1000000007

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tests = 1; tests <= t; tests++)
	{
		ll n;
		scanf("%lld", &n);
		ll temp = n;
		int count = 0;
		if(n==0)
			printf("Case #%d: INSOMNIA\n", tests);
		else
		{
			map<int, int> check;
			int i;
			for (i = 1; count < 10; i++)
			{
				temp = n*i;
				while (temp > 0)
				{
					int r = temp % 10;
					temp /= 10;
					if (check[r] == 0)
						check[r] = 1, count++;
				}
			}
			printf("Case #%d: %lld\n", tests,n*(i-1));
		}
	}
	return 0;
}