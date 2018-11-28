#pragma comment(linker, "/STACK:100000000")
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

typedef long long ll;
#define mod 1000000007
#define INF mod
#define pi acos(-1.0)
#define LINF 1000000000000000000LL
#define eps 1e-10



int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int n;
		scanf("%d", &n);
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}
		ll i;
		int mask = 0;
		for(i = n; ; i += n)
		{
			ll k = i;
			while(k)
			{
				mask |= (1 << (k % 10));
				k /= 10;
			}
			if(mask == 1023)
				break;
		}
		printf("Case #%d: %lld\n", t, i);
	}
	return 0;
}