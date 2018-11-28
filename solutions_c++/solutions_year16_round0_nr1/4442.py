#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for (int j = 1; j <= t; ++j)
	{
		printf("Case #%d: ",j);
		long long int n,k,l=1,w;
		scanf("%lld",&n);
		if(n==0)
			printf("INSOMNIA\n");
		else
		{
			k=n;
			int a[10];
			for (int i = 0; i < 10; ++i)
				a[i]=0;
			while((a[0]==0) || (a[1]==0) || (a[2]==0) || (a[3]==0) || (a[4]==0) || (a[5]==0) || (a[6]==0) || (a[7]==0) || (a[8]==0) || (a[9]==0))
			{
				long long int i=k*l;
				w=i;
				while(i)
				{
					int t=i%10;
					i/=10;
					a[t]++;
				} 
				l++;
			}
			printf("%lld\n",w);
		}
	}
}