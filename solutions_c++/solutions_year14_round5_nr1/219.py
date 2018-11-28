#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
int main()
{
	FILE *fr=fopen("a-large.in","r");
	FILE *fw=fopen("out1.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int t=0;t<data;t++)
	{
		int num;
		fscanf(fr,"%d",&num);
		vector<ll>vec;
		int p,q,r,s;
		fscanf(fr,"%d%d%d%d",&p,&q,&r,&s);
		ll now=q%r;
		for(int i=0;i<num;i++)
		{
			vec.push_back(now+s);
			now+=p;
			now%=r;
		}
		vector<ll>rui;
		rui.push_back(0);
		for(int i=0;i<num;i++)
		{
			rui.push_back(rui[i]+vec[i]);
		}
		int pt=0;
		ll mini=1000000000000000000LL;
		for(int i=0;i<=num;i++)
		{
			for(;;)
			{
				mini=min(mini,max(rui[i],max(rui[pt]-rui[i],rui[num]-rui[pt])));
				if(rui[pt]-rui[i]<rui[num]-rui[pt])
				{
					pt++;
				}
				else
				{
					break;
				}
			}
		}
		fprintf(fw,"Case #%d: %.12lf\n",t+1,double(rui[num]-mini)/double(rui[num]));
	}
}