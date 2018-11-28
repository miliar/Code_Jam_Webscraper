#include<bits/stdc++.h>
using namespace std;
int flag[10];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int k=1;
	scanf("%d",&t);
	while(t--){
		long long n;
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",k++);
			continue;
		}
		long long int i,j;
		for(i=0;i<=9;i++)
		flag[i]=0;
		i=1;
		long long x;
		while(1)
		{
			j=i*n;
			int co=0;
			while(j!=0)
			{
				int d=j%10;
				flag[d]=1;
				j=j/10;
			}
			for(j=0;j<=9;j++)
			{
				if(!flag[j])
				{
					co=1;
					break;
				}
			}
			if(co==0)
			{
				x=i*n;
				break;
			}
			i++;
		}
		printf("Case #%d: %lld\n",k++,x);
	}
	return 0;
}
