#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,cnt=1;
	cin>>t;
	while(t--)
	{
		int n,c=0,a,i,j,b,k;
		scanf("%d%d%d",&a,&b,&k);
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
					c++;
			}
		}
		printf("Case #%d: %d\n",cnt++,c);;
	}
	return 0;
}