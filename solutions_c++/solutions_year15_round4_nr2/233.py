#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
typedef long double ld;
typedef pair<ld,ld>pld;
ld eps=1e-13;
int main()
{
	FILE *fr=fopen("B-large.in","r");
	FILE *fw=fopen("outl.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=1;p<=data;p++)
	{
		int num;
		ld mv,mx;
		fscanf(fr,"%d%Lf%Lf",&num,&mv,&mx);
		ld mini=200,maxi=-200;
		vector<pld>vec;
		for(int i=0;i<num;i++)
		{
			ld za,zb;
			fscanf(fr,"%Lf%Lf",&za,&zb);
			vec.push_back(make_pair(zb,za));
		}
		sort(vec.begin(),vec.end());
		ld beg=0.0,end=1000000000000000.0;
		for(int q=0;q<200;q++)
		{
			ld med=(beg+end)/2.0;
			ld now=mv;
			ld sum1=0.0;
			for(int i=0;i<vec.size();i++)
			{
				if(now>med*vec[i].second)
				{
					now-=med*vec[i].second;
					sum1+=med*vec[i].second*vec[i].first;
				}
				else
				{
					sum1+=now*vec[i].first;
					now=0;
				}
			}
			ld sum2=0.0;
			now=mv;
			for(int i=vec.size()-1;i>=0;i--)
			{
				if(now>med*vec[i].second)
				{
					now-=med*vec[i].second;
					sum2+=med*vec[i].second*vec[i].first;
				}
				else
				{
					sum2+=now*vec[i].first;
					now=0;
				}
			}
			if(sum1*(1.0-eps)<=mv*mx&&mv*mx<=sum2*(1.0+eps))
			{
				end=med;
			}
			else
			{
				beg=med;
			}
		}
		if(beg>=900000000000000.0)fprintf(fw,"Case #%d: IMPOSSIBLE\n",p);
		else fprintf(fw,"Case #%d: %.10Lf\n",p,beg);
	}
}