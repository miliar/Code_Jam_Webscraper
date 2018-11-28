#include<cstdio>
#include<vector>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
#define PB push_back
int main()
{
	double wn[1010],wk[1010];
	double x;
	int n,t,ans2,p=1,ans1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",wn+i);
		for(int i=0;i<n;i++)
			scanf("%lf",wk+i);
		sort(wn,wn+n);
		sort(wk,wk+n);
		/*for(int i=0;i<n;i++)
			printf("%lf ",wn[i]);
		printf("\n");

		for(int i=0;i<n;i++)
			printf("%lf ",wk[i]);
		printf("\n");*/
		int p_j=-1,c=0;
		int i=0,j=0;
		while(i<n && j<n)
		{
			if(wn[i]>wk[j])
			{
				c++;
				i++;
				j++;
			}
			else
				i++;
		}
		ans1=c;
		c=0;
		for(int i=0;i<n;i++)
		{
			for(int j=p_j+1;j<n;j++)
			{
				if(wk[j]>wn[i])
				{
					p_j=j;
					c++;
					break;
				}
			}
		}
		ans2=n-c;
		printf("Case #%d: %d %d\n",p++,ans1,ans2);
	}
	return 0;
}

