#include <iostream>
#include<algorithm>
#include <cstdio>
#include <vector>
using namespace std;
int main()
{
	int t,n,j,ans1,ans2,e,x,y;
	scanf("%d",&t);
	for(e=1;e<=t;e++)
	{
		ans1=0;
		ans2=0;
		scanf("%d",&n);
		vector <float> nao(n),ken(n);
		for(j=0;j<n;j++)
		scanf("%f",&nao[j]);
		for(j=0;j<n;j++)
		scanf("%f",&ken[j]);
		sort(nao.begin(),nao.end());
		sort(ken.begin(),ken.end());
		x=0;
		y=0;
		while(1)
		{
			if(ken[y]<nao[x])
			{
				ans1+=1;
                           x+=1;
                          y+=1;
			}
			else
                        	x+=1;
			if(x==n||y==n)
                         break;
		}
		x=0;
		y=0;
		while(1)
		{
			if(ken[y]>nao[x])
			{
				ans2++;
                           x++;
                    	y++;
			}
			else
                         y++;
			if(x==n||y==n)
                         break;
		}
		printf("Case #%d: %d %d\n",e,ans1,n-ans2);
		nao.clear();
		ken.clear();
	}
	return 0;
}
