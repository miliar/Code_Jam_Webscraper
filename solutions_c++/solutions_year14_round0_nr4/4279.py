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

bool desc(double a, double b)
{
	return a>b;
}
main()
{
	int tc;
	cin>>tc;
	for(int t = 1;t<=tc;t++)
	{
		int n;
		cin>>n;
		double arr1[n], arr2[n];
		for(int i = 0;i<n;i++)
			scanf("%lf", &arr1[i]);
		for(int i = 0;i<n;i++)
			scanf("%lf", &arr2[i]);
		sort(arr1, arr1+n, desc);
		sort(arr2, arr2+n, desc);
		int dw = 0, w = 0;
		int k = 0;
		for(int i = 0;i<n && k < n;i++)
		{
			while(arr1[i] < arr2[k])
				k++;
			if(k >= n)
				break;
			k++;
			dw++;
		}
		k = 0;
		for(int i = 0;i<n;i++)
		{
			if(arr1[i] > arr2[k])
				w++;
			else
				k++;
		}
		printf("Case #%d: %d %d\n", t,dw,w);
	}
}
