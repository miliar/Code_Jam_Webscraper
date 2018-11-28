#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);

	for(int i=0;i<t;i++)
	{
		int n;
		scanf("%d",&n);

		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}

		int a[10]={0},cx=n,ay=n;

		while(cx)
		{
			a[cx%10]++;
			cx=cx/10;
		}

		int c=1;

		while(true)
		{
			bool f=false;
			for(int j=0;j<10;j++)
				if(a[j]<=0)
				{
					f=true;
					break;
				}
			if(!f)
				break;
			n=n+ay;
			cx=n;
			while(cx)
			{
				a[cx%10]++;
				cx=cx/10;
			}

			c=c+1;
			//printf("%d\n",n);
		}

		printf("Case #%d: %d\n",i+1,n);

	}

	return 0;
}



			

