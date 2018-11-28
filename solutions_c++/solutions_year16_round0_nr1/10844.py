#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,k=1,cnt,rem;
	long long int n , x, i, num;
	int mapNum[12];
	scanf("%d",&t);
	while(t--)
	{
		scanf("%lld",&num);
		cnt = 0;
		for(i=0;i<12;i++)
			mapNum[i] = 0 ;
		i=2;
		if(num == 0)
			printf("Case #%d: INSOMNIA\n",k);
		else
		{
			cnt=0;
			n=num;
			while(cnt<10)
			{
				x=n;
			//	cout<<x<<"\n";
				while(x)
				{
					rem = x%10;
					if(mapNum[rem]==0)
					{
						cnt++;
						mapNum[rem]=1;
					}
					x = x/10;
					
				}
				if(cnt == 10)
					break;
				n =i*num;
				i++;
			}
			printf("Case #%d: %lld\n",k, n);
		}
		k++;
	}
	
//	system("Pause");
	return 0;
}
