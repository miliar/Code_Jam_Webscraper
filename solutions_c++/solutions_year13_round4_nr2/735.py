#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <sstream>

using namespace std;

const int NMAX = 1000;



long long best[NMAX], bestind[NMAX], worst[NMAX], worstind[NMAX];

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d\n", &t);

	for (int test = 0; test < t; test++)
	{
		long long n, p, ans1 = -1, ans2 = -1;
		cin>>n>>p;

		bestind[0] = 0;
		best[0] = 1;
		long long pos = (1LL << n);

		for (int i = 1; i <= n; i++)
		{
			pos /= 2LL;
			bestind[i] = bestind[i-1] + pos;
			best[i] = best[i-1] * 2LL;
		}

		int i = 0;
		while (p >= best[i] && i <= n)
		{
			ans1 = bestind[i];
			i++;
		}

		worstind[0] = 0;
		worst[0] = 1;
		long long powe = 1LL;
		pos = (1LL << n);

		for (int i = 1; i < n; i++)
		{
			powe *= 2LL;
			worstind[i] = worstind[i-1] + powe;
			pos /= 2LL;
			worst[i] = worst[i-1] + pos;
		}
		worst[n] = (1LL << n);
		worstind[n] = worst[n] - 1;
		i = 0;
		while (p >= worst[i] && i <= n)
		{
			ans2 = worstind[i];
			i++;
		}

		cout<<"Case #"<<test+1<<": "<<ans2<<" "<<ans1<<endl;
	
		//printf("Case #%d: %d %d\n", test +1, ans1, ans2);
	}


	return 0;
}