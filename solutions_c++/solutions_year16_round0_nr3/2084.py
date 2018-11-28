#include<bits/stdc++.h>
using namespace std;
int pie[10001];
int sit[10005];
int pom=10001;
char ss[40];
long long dziel[11];
int ile=0;
int main()
{
	for(int i=2; i<=pom; i++)
		{
			if(sit[i]==0)
			{
				ile++;
				pie[ile]=i;
				//printf("%d\n", ile);
			}
			for(int j=i; j<=pom; j+=i)
				sit[j]=1;
		}
	//printf("%d\n", ile);
	int n;
	int wyn=0,kon;
	scanf("%d", &n);
	scanf("%d%d", &n, &kon);
	long long p=1;
	for(int i=1; i<n; i++)
		p*=2;
	printf("Case #1:\n");
	for(long long i=p+1; i<2*p; i++)
	{
		if(i%2==0) continue;
		long long s=0;
		long long h=1;
		int czy=1;
		for(long long j=2; j<=10; j++)
		{
			int c2=0;
			for(int oo=1; oo<=ile; oo++)
			{
				h=1;
				long long x=i;
				s=0;
				for(int o=1; o<=n; o++)
				{
					if(x%2==1)
						s=(s+h)%pie[oo];
						h=(h*j)%pie[oo];
					x/=2;
				}
				//printf("%d %lld\n", i, s);	
				if(s%pie[oo]==0)
				{
					dziel[j]=pie[oo];
					c2=1;
					break;
				}
			}
			czy=c2;
			if(czy==0)
				break;
		}
		long long x=i;
		if(czy==1)
		{
			wyn++;
			for(int o=1; o<=n; o++)
			{
				if(x%2==1)
					ss[n-o]='1';
				else
					ss[n-o]='0';
				x/=2;
			}
			printf("%s ", ss);
			for(int o=2; o<=10; o++)
				printf("%lld ", dziel[o]);
			printf("\n");
		}
		if(wyn==kon)
			break;
	}

}
