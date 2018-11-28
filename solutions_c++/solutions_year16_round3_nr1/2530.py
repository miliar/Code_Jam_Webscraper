
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;


int main()
{
	freopen("A-small-practice.in","rt",stdin);
	freopen("aout.out","wt",stdout);
	int t,i,j,max[2],secmax[2];
	int n,a[30];
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%d",&n);
		printf("Case #%d: ",j);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		if(a[0]>a[1])
		{
			max[0]=a[0];
			secmax[0]=a[1];
			max[1]=0;
			secmax[1]=1;
		}
		else
		{
			max[0]=a[1];
			secmax[0]=a[0];
			max[1]=1;
			secmax[1]=0;
		}
	//	printf("%d %d %d %d\n",max[0],max[1],secmax[0],secmax[1]);
		for(i=2;i<n;i++)
		{
			if(max[0]<a[i])
			{
				secmax[0]=max[0];
				secmax[1]=max[1];
				max[0]=a[i];
				max[1]=i;
			}
			else
			{
				if(secmax[0]<a[i])
				{
					secmax[0]=a[i];
					secmax[1]=i;
				}
			}
		}
	//	printf("%d %d %d %d\n",max[0],max[1],secmax[0],secmax[1]);
		while(a[max[1]]>a[secmax[1]])
		{
			a[max[1]]--;
			printf("%c ",'A'+max[1]);
		}
		for(i=0;i<n;i++)
		{
			if(i==max[1]||i==secmax[1])
			continue;
			while(a[i]!=0)
			{
				a[i]--;
				printf("%c ",'A'+i);
			}
		}
		while(a[max[1]]!=0)
		{
			a[max[1]]--;
			a[secmax[1]]--;
			printf("%c%c ",'A'+max[1],'A'+secmax[1]);
		}
		printf("\n");
	}
	return 0;
}
