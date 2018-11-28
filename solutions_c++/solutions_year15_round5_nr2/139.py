#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
using namespace std;
typedef long long ll;
int main()
{
	FILE *fr=fopen("B-large.in","r");
	FILE *fw=fopen("outl.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		int num,kai;
		fscanf(fr,"%d%d",&num,&kai);
		vector<ll>vec;
		for(int i=0;i<num-kai+1;i++)
		{
			int zan;
			fscanf(fr,"%d",&zan);
			vec.push_back(zan);
		}
		ll mx[100],mn[100];
		fill(mx,mx+100,0);
		fill(mn,mn+100,0);
		ll maxi=-1,rr=-1;
		for(int i=0;i<kai;i++)
		{
			ll now=0;
			for(int j=i;j<vec.size()-1;j+=kai)
			{
				now+=vec[j+1]-vec[j];
				mx[i]=max(mx[i],now);
				mn[i]=min(mn[i],now);
			}
			//printf("%d %d\n",mx[i],mn[i]);
			if(maxi<mx[i]-mn[i])
			{
				maxi=mx[i]-mn[i];
				rr=i;
			}
		}
		ll amx=0,ami=0;
		for(int i=0;i<kai;i++)
		{
			amx+=mx[rr]-mx[i];
			ami+=mn[rr]-mn[i];
		}
		//printf("%d %d\n",ami,amx);
		ll ans;
		if(amx-ami>=kai)ans=maxi;
		else
		{
			ans=maxi+1;
			for(ll i=ami;i<=amx;i++)
			{
				if((vec[0]%kai+kai)%kai==(i%kai+kai)%kai)ans=maxi;
			}
		}
		fprintf(fw,"Case #%d: %lld\n",p+1,ans);
	}
}