#include<iostream>
#include<cstdio>
#include<list>
using namespace std;

int main()
{
	int kase = 1, t;
	scanf("%d",&t);
	
	while(t--)
	{
		double naomi[1010] = {0.0000000};
		double ken[1010] = {0.0000000};
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&naomi[i]);
		}
		for(int i=0;i<n;i++)
		{
			scanf("%lf",&ken[i]);
		}
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		int war = 0;
		int nS = 0, nE = n-1, kS = 0, kE = n-1;
		for(int i=0;i<n;i++)
		{
			if(naomi[nE] > ken[kE])
			{
				war++;
				nE--;
				kS++;
			}
			else
			{
				nE--;
				kE--;
			}
		}
		int dWar = 0;
		nS = 0, nE = n-1, kS = 0, kE = n-1;
		for(int i=0;i<n;i++)
		{
			if(naomi[nS] < ken[kS])
			{
				nS++;
				kE--;
			}else if(naomi[nE] < ken[kE])
			{
				nS++;
				kE--;
			}else
			{
				nE--;
				kE--;
				dWar++;
			}
		}
		printf("Case #%d: ",kase);
		printf("%d %d\n",dWar, war);
		kase++;
	}
	return 0;
}
