#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("oa.txt", "w", stdout);
	long long i, j, k, N, nn, cases;
	int a[15];
	scanf("%lld",&cases);

	for(int t = 1;t<=cases;t++)
	{
		scanf("%lld",&N);

		if(N == 0)
		{
			printf("Case #%d: INSOMNIA\n", t);
			continue;
		}

		for(i = 0;i<=10;i++) a[i] = 0;

		j = 1;
		nn = N;
		while(1)
		{
			long long n = N;
			//printf("n = %lld\n", n);
			while(n > 0)
			{
				a[n%10] = 1;
				n = n/10;
			}
			int flag = 1;
			for(i = 0;i<=9;i++)
			{
				if(a[i] == 0) {
					flag = 0;
					break;
				}
			}

			if(flag) break;

			j+=1;
			N = j*nn;
		}

		printf("Case #%d: %lld\n",t,N);

	}

	return 0;
}
