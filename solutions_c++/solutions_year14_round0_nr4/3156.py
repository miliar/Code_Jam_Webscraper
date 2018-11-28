#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <cstdlib>
#include <map>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int n;
		scanf("%d",&n);
		double a[n],b[n];
		for(int j=0;j<n;j++)
			scanf("%lf",&a[j]);
		for(int j=0;j<n;j++)
			scanf("%lf",&b[j]);
		sort(a,a+n);
		sort(b,b+n);
		int pointa1=0,pointa2=0;
		int ptr=n-1,min_ptr=0,max_ptr=n-1;
		for(int j=n-1;j>-1;j--)
		{
			if(b[j]<a[ptr])
			{
				pointa1++;
				ptr--;
			}
			if(a[j]>b[max_ptr])
			{
				pointa2++;
				min_ptr++;
			}
			else
				max_ptr--;
		}
		
		printf("Case #%d: %d %d\n",i+1,pointa1,pointa2);
	}
}
