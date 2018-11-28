#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iomanip>
#include<functional>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<limits>
#include<climits>
using namespace std;

long long tc, n;
string str;
int main()
{
#ifdef _CONSOLE
	//freopen("input.txt", "r", stdin);
	freopen("C:\\Users\\Sangyun\\Desktop\\input.in", "r", stdin);
	freopen("C:\\Users\\Sangyun\\Desktop\\out.out", "w+", stdout);
#endif
	////////////////////////////////////////////////////// 
	scanf("%lld", &tc);
	for (long long i = 1; i <= tc; i++)
	{
		scanf("%d", &n);
		cin >> str;
		long long sum = 0;
		long long res = 0;
		for (long long i = 0; i <= n; i++)
		{
			if (sum >= i)
			{
				sum += str[i] - '0';
				continue;
			}
			else
			{
				sum++;
				sum += str[i] - '0';
				res++;
			}
		}
		printf("Case #%lld: %lld\n", i, res);
	}
	
}