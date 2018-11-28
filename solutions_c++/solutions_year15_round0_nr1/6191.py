#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#define s(x) scanf("%d",&x)
using namespace std;

int main()
{
	int t;
	s(t);
	int j,i;
	for(j=1;j<=t;j++)
	{
		int n;
		scanf("%d",&n);
		char A[20000];
		scanf("%s",&A);
		int r=0,c=0;
		//printf("%s\n",A);
		for(i=0;i<=n;i++)
		{
			if(r<i)
			{
				c++;
				r++;
			}
			r=r+(int)(A[i]-48);
			//printf("%d ",r);
		}
		printf("Case #%d: %d\n",j,c);
;	}
	return 0;
}
