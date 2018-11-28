using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>

typedef long long L;
typedef unsigned long long U;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

int arr[10007];
main()
{
	int tc;
	cin>>tc;
	for(int t = 1;t <= tc; t++)
	{
		int n,x;
		cin>>n>>x;
		for(int i = 0;i< n;i++)
			scanf("%d", &arr[i]);
		sort(arr, arr+n);
		int s = 0, e = n-1, c = 0;
		while(s <= e)
		{
			if(arr[s] + arr[e] <= x)
			{
				c++;
				s++;
				e--;
			}
			else
			{
				c++;
				e--;
			}
		}
		printf("Case #%d: %d\n", t, c);
	}
}
