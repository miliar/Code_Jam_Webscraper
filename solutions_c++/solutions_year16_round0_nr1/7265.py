#include<iostream>
using namespace std;

int check(int d[])
{
	int i;
	for(i=0;i<10;i++)
		if(d[i]==0)
			break;
	if(i==10)
		return 1;
	return 0;
}


int main()
{
	int u,t;
	cin>>u;

	for(t=1;t<=u;t++)
	{
		int d[10]={0};
		long long n,c=1,l;
		cin>>n;
		if(n==0)
			{
				printf("Case #%d: INSOMNIA\n",t);
				continue;
			}
		while(!check(d))
		{
			long long k=n*c;
			l=n*c;
			c++;
			while(k!=0)
			{
				d[k%10]++;
				k=k/10;
			}
		}
		printf("Case #%d: %lld\n",t,l);	


	}
}