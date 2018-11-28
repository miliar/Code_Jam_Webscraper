#include<map>
#include<set>
#include<iostream>
#include<string.h>
#include<string>
#include<queue>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<memory.h>
#include <iomanip>
using namespace std;

#define mp make_pair
#define X first
#define Y second

double const eps = 1e-10;
int const INF = 100000;
int const MOD = 1;
int const MAX = 5*100*1000 + 5;

int main()
{
#ifdef _DEBUG
    freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
#endif
	int t, tt;
	scanf("%d", &t);
	for(tt = 0; tt < t; ++tt)
	{
		printf("Case #%d: ", tt + 1);
		int k, a, b, i, j, n = 0;
		scanf("%d%d%d", &a, &b, &k);
		for(i = 0; i < a; ++i)
			for(j = 0; j < b; ++j)
				if((i & j) < k)
					++n;
		
		printf("%d\n", n);
	}

	return 0;
}