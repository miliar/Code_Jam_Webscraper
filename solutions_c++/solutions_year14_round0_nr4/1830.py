# include<cstdio>
# include<cmath>
# include<algorithm>
using namespace std;
int main()
{
	int i,j,k;
	int t,n,war,dwar;
	double nao[1001], ken[1001];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		war = 0,dwar = 0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&nao[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&ken[i]);
		sort(nao,nao+n);
		sort(ken,ken+n);
		/*
		for(i=0;i<n;i++)
			printf("%lf ",nao[i]);
		printf("\n");
		for(i=0;i<n;i++)
			printf("%lf ",ken[i]);
		printf("\n\n");
		*/
		i=0,j=0;
		while(i<n && j<n)
		{
			if(nao[i] > ken[j])
				j++;
			else
			{
				i++;
				j++;
			}
		}
		war = n-i;
		i=0,j=0;
		int m=n;
		while(i<n && j<m)
		{
			if(nao[i] > ken[j])
			{
				i++;
				j++;
				dwar++;
			}
			else
			{
				m--;
				i++;
			}
		}
		printf("Case #%d: %d %d\n",k,dwar,war);
	}
	return 0;
}