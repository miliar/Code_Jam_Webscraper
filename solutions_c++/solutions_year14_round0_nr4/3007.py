#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

double Naomi[10000], Ken[10000];
int n;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("DLarge.out","w",stdout);
	
	int test;
	scanf("%d",&test);
	for(int p=1; p<=test; p++)
	{
		scanf("%d",&n);
		for(int i=0; i<n; i++)
		{
			scanf("%lf",&Naomi[i]);
		}
		for(int i=0; i<n; i++)
		{
			scanf("%lf",&Ken[i]);
		}
		sort(Naomi, Naomi+n);
		sort(Ken, Ken+n);

		int ken_points_w = 0;
		int naomi_dw = 0;
		int ken_points_dw = 0;

		int l = 0;
		for(int j=0; j<n && l<n; j++)
		{
			while(l<n && Ken[l] < Naomi[j])
			{
				l++;
			}
			if(l<n && Ken[l] > Naomi[j])
			{
				ken_points_w++;
				l++;
			}
		}
		int l_k = 0;
		int l_n = 0;

		while(ken_points_dw + naomi_dw < n)
		{
			if(Naomi[l_n] > Ken[l_k])
			{
				l_n++;
				l_k++;
				naomi_dw++;
			}
			else
			{
				ken_points_dw++;
				l_n++;
			}
		}
		
		printf("Case #%d: %d %d\n",p,naomi_dw,n-ken_points_w);

	}


return 0;
}