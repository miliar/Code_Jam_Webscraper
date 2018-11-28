#include<iostream>
#include<cstring>
#include<queue>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<set>
#define N 1005
using namespace std;
int t,n;
set<double > s1,s2,ss1,ss2;
//double ss1[N],ss2[N];
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int time=0;
	while(t--)
	{
		scanf("%d",&n);
		s1.clear();
		s2.clear();  ss1.clear(); ss2.clear();
		double tmp;
		for(int i=1;i<=n;i++)
		{
			scanf("%lf",&tmp);
			s1.insert(tmp); ss1.insert(tmp);//ss1[i]=tmp;
		}
		for(int i=1;i<=n;i++)
		{
			scanf("%lf",&tmp);
			s2.insert(tmp); ss2.insert(tmp);//ss2[i]=tmp;
		}
		/*
		int ad=0;
		for(set<double > ::iterator it=s1.begin();it!=s1.end(); it++)
			ss1[++ad]=*it;
		ad=0;
		for(set<double > ::iterator it=s2.begin();it!=s2.end(); it++)
			ss2[++ad]=*it;
		*/
		int ans1,ans2;
		ans1=ans2=0;
		for(set<double > ::iterator it=s1.begin();it!=s1.end(); it++)
		{
			set<double > ::iterator a=lower_bound(s2.begin(),s2.end(),*it);// printf("%lf !\n",*it);
			if(a==s2.end())
			{
				ans1++;  s2.erase(s2.begin());//s1.erase(it);
			}
			else
			{
				s2.erase(a);//s1.erase(it);
			}
		}
		//for(int i=1;i<=n;i++) printf("%lf  ",ss1[i]); puts("");
		//for(int i=1;i<=n;i++) printf("%lf  ",ss2[i]) ; puts("");
		/*int mark=-1;
		for(int i=1;i<=n;i++)
		{
			int next=n-i+1;
			if(ss1[i]>ss2[1])
			{
				mark=i; break;
			}
		}
		//printf("m: %d \n",mark);
		if(mark==-1) ans2=0;
		else
		{
			ans2=n-mark+1;
		}*/
		for(set<double > ::iterator it=ss1.begin();it!=ss1.end();it++)
		{
			if(*it> *ss2.begin())
			{
				ans2++; ss2.erase(ss2.begin());
			}
			else
			{
				double dd=*(--ss2.end());
				ss2.erase(dd);
			}
		}
		printf("Case #%d: %d %d\n",++time,ans2,ans1);
	}


    return 0;
}
