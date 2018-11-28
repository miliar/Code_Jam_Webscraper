#include<iostream>
#include<cstdio>
#include<vector>
#include<utility>
#include<algorithm>
#define ll long long
using namespace std;

int main()
{
	//freopen("R12L.in", "r", stdin);
	//freopen("R12L.out", "w", stdout);
	ll T,basis,it,max,i,N,temp,j;
	vector<ll> vec;
	scanf("%lld", &T);
	for(it = 1; it <= T; it++)
	{
		ll arr[2501] = {0};
		vec.clear();
		scanf("%lld", &N);
		for(i = 0; i < (2*N - 1); i++)
		{
			for(j = 0;j < N; j++)
			{
				scanf("%lld", &temp);
				arr[temp]++;
			}
		}
		for(i = 0; i < 2501; i++)
		{
			if(arr[i] % 2 != 0)
				vec.push_back(i);
		}
		sort(vec.begin(),vec.end());
		printf("Case #%lld: ", it);
		for(i = 0; i < vec.size(); i++)
			printf("%lld ",vec[i]);
		putchar('\n');
	}
	return 0;
}
