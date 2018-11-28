#include<stdio.h>
#include "stdafx.h"
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
typedef long long ll;
typedef pair<ll,ll>pii;
typedef pair<ll,vector<ll> >piv;
int main()
{
	FILE *fr=fopen("D-small-attempt0.in","r");
	FILE *fw=fopen("outs.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		printf("%d\n",p);
		int num;
		fscanf(fr,"%d",&num);
		vector<pii>vec;
		for(int i=0;i<num;i++)
		{
			ll zan;
			fscanf(fr,"%lld",&zan);
			vec.push_back(make_pair(zan,0));
		}
		for(int j=0;j<num;j++)
		{
			ll zan;
			fscanf(fr,"%lld",&zan);
			vec[j].second=zan;
		}
		sort(vec.begin(),vec.end());
		ll dat[61];
		dat[0]=1;
		for(int i=1;i<=60;i++)dat[i]=dat[i-1]*2;
		int n0;
		for(int i=0;i<=60;i++)if(vec[0].second==dat[i])n0=i;
		for(int i=0;i<vec.size();i++)vec[i].second/=dat[n0];
		map<ll,ll>ma;
		for(int i=0;i<vec.size();i++)
		{
			ma[vec[i].first]=vec[i].second;
		}
		vector<piv>now;
		piv dam;
		dam.first=0;
		now.push_back(dam);
		ll nsz=0;
		for(int i=0;i<vec.size();i++)nsz+=vec[i].second;
		for(;;)
		{
			if(nsz==1)break;
			nsz/=2;
			map<ll,ll>::iterator it=ma.begin();
			ll fl=0,beg,nx;
			for(;;)
			{
				if((*it).second!=0)
				{
					if(fl==0)
					{
						beg=(*it).first;
						fl=1;
					}
					else if(fl==1)
					{
						nx=(*it).first;
						break;
					}
				}
				it++;
			}
			ll ad=nx-beg;
			//printf("  %lld\n",ad);
			map<ll,ll>nma;
			it=ma.begin();
			for(;;)
			{
				if(it==ma.end())break;
				if((*it).second!=0)
				{
					ma[(*it).first+ad]-=(*it).second;
					nma[(*it).first]=(*it).second;
				}
				it++;
			}
			ma=nma;
			it=ma.begin();
			for(;;)
			{
				if(it==ma.end())break;
				it++;
			}
			vector<piv>nnow;
			for(int i=0;i<now.size();i++)
			{
				if(nma[now[i].first]!=0)
				{
					nnow.push_back(make_pair(now[i].first,now[i].second));
					nnow[nnow.size()-1].second.push_back(ad);
				}
				if(nma[now[i].first-ad]!=0)
				{
					nnow.push_back(make_pair(now[i].first-ad,now[i].second));
					nnow[nnow.size()-1].second.push_back(-ad);
				}
			}
			sort(nnow.begin(),nnow.end());
			now=nnow;
		}
		vector<ll>ans;
		ans=now[0].second;
		for(int i=0;i<now.size();i++)
		{
			sort(now[0].second.begin(),now[0].second.end());
			for(int j=0;j<now[i].second.size();j++)
			{
				if(ans[j]>now[i].second[j])
				{
					ans=now[i].second;
					break;
				}
			}
		}
		fprintf(fw,"Case #%d:",p+1);
		for(int i=0;i<ans.size();i++)
		{
			if(ans[i]<0)fprintf(fw," %lld",ans[i]);
		}
		for(int i=0;i<n0;i++)fprintf(fw," 0");
		for(int i=0;i<ans.size();i++)
		{
			if(ans[i]>0)fprintf(fw," %lld",ans[i]);
		}
		fprintf(fw,"\n");
	}
}