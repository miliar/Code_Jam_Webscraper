#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf ("%d",&t);
	int t1 = t;
	while(t--)
	{
		long long int n,i;
		scanf ("%lld",&n);
		int a[100];
		for(i=0;i<20;i++)
			a[i] = 0;
		long long  ans = -1;
		long long  count = 0;
		for(i=1;i<=10000;i++)
		{
			long long  temp = n * i;
			while(temp!=0)
			{
				long long  temp2 = temp%10;
				temp/=10;
				if(a[temp2]==0)
				{
//					printf("here for %d %d\n",i,temp2);
					a[temp2] = 1;
					count++;
					if(count == 10)
						ans = i;
				}
			}
			if(ans!=-1)
				break;
		}
		printf("Case #%d: ",t1-t);
		if(ans==-1)
			printf("INSOMNIA\n");
		else
			printf("%lld\n",ans*n);
	}	
	

	return 0;
}