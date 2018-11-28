#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int t;
int main()
{
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n,war=0,deceitful_war=0;
		double naomi[1000],ken[1000];
		scanf("%d",&n);
		for(int j=0;j<n;j++) cin>>naomi[j];
		for(int j=0;j<n;j++) cin>>ken[j];
		sort(naomi,naomi+n);
		sort(ken,ken+n);

		//Deceitful War
		int ni=0,k=0;
		while(1)
		{
			if(ni == n || k == n) break;
			if(naomi[ni] > ken[k])
			{
				deceitful_war++;
				ni++;
				k++;
			}
			else 
			{
				ni++;
			}
		}

		//War
		ni=0;k=0;
		while(1)
		{
			if(k == n || ni == n) break;
			if(ken[k] > naomi[ni])
			{
				war++;
				ni++;
				k++;
			}
			else
			{
				k++;
			}
		}
		war = n - war;
		printf("Case #%d: %d %d\n",i+1,deceitful_war,war);
	}
	return 0;
}