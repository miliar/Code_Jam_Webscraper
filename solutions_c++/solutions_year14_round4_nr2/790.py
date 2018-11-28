#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#define N 10

using namespace std;

int T,i,ml,mr,j,a[2000],n,ans,ts;

int main()
{
	freopen("b.in","r",stdin);	freopen("b.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		ans=0;
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=0;i<n;i++)
		{
			ml=mr=0;
			for(j=0;j<i;j++)
				if(a[j]>a[i])
					ml++;
			for(j=i+1;j<n;j++)
				if(a[j]>a[i])
					mr++;
			ans+=min(ml,mr);
		}
		printf("Case #%d: %d\n",++ts,ans);
	}
	return 0;
}
