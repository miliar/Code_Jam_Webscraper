#include<stdio.h>
#include "stdafx.h"
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
typedef long long ll;
typedef pair<ll,ll>pii;
typedef pair<pii,pii>pi4;
#define INF 1000000000000000000LL
bool flag[1002];
ll dist[1002];
ll map[1002][1002];
ll calc(pi4 a,pi4 b)
{
	if(a.first.first>b.first.first)
	{
		swap(a,b);
	}
	if(a.first.second>b.first.second)
	{
		a.first.second=-a.first.second;
		a.second.second=-a.second.second;
		b.first.second=-b.first.second;
		b.second.second=-b.second.second;
		swap(a.first.second,a.second.second);
		swap(b.first.second,b.second.second);
	}
	return max(b.first.first-a.second.first,b.first.second-a.second.second)-1;
}
int main()
{
	FILE *fr=fopen("c-large.in","r");
	FILE *fw=fopen("out.txt","w");
	int data;
	fscanf(fr,"%d",&data);
	for(int p=0;p<data;p++)
	{
		int mx,my,num;
		fscanf(fr,"%d%d%d",&mx,&my,&num);
		vector<pi4>vec;
		for(int i=0;i<num;i++)
		{
			int za,zb,zc,zd;
			fscanf(fr,"%d%d%d%d",&za,&zb,&zc,&zd);
			vec.push_back(make_pair(make_pair(za,zb),make_pair(zc,zd)));
		}
		map[0][0]=map[1][1]=INF;
		map[0][1]=map[1][0]=mx;
		for(int i=0;i<num;i++)
		{
			map[0][i+2]=map[i+2][0]=vec[i].first.first;
			map[i+2][1]=map[1][i+2]=mx-vec[i].second.first-1;
		}
		for(int i=0;i<num;i++)
		{
			for(int j=0;j<num;j++)
			{
				if(i!=j)
				{
					map[i+2][j+2]=calc(vec[i],vec[j]);
				}
				else
				{
					map[i+2][j+2]=INF;
				}
			}
		}
		//for(int i=2;i<num+2;i++){for(int j=2;j<num+2;j++)printf("%lld ",map[i][j]);printf("\n");}
		fill(flag,flag+num+2,false);
		fill(dist,dist+num+2,INF);
		dist[0]=0;
		for(;;)
		{
			ll mini=INF;
			int rr=-1;
			for(int i=0;i<num+2;i++)
			{
				if(mini>dist[i]&&(!flag[i]))
				{
					mini=dist[i];
					rr=i;
				}
			}
			if(rr==1)
			{
				fprintf(fw,"Case #%d: %lld\n",p+1,dist[rr]);
				break;
			}
			flag[rr]=true;
			for(int i=0;i<num+2;i++)
			{
				dist[i]=min(dist[i],dist[rr]+map[rr][i]);
			}
		}
	}
}