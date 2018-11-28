#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
typedef long long LL;
#define N 10010
int T,n,m;
LL ans,total;

struct node { int s,e,p; } rec[N];
bool cmp(node a,node b)
{
	return a.s==b.s?a.e>b.e:a.s<b.s;
}

LL calc(LL s,LL t)
{
	if (s==t) return 0;
	t-=s+1;
	LL ret=t*(t+1)/2;
	return ret;
}

int main()
{
	cin>>T;
	for (int t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&m);
		total=ans=0;
		for (int i=0;i<m;i++) 
		{
			scanf("%d%d%d",&rec[i].s,&rec[i].e,&rec[i].p);
			total+=calc(rec[i].s,rec[i].e)*rec[i].p;
		}
		for (int i=m-1;i>=0;i--)
			for (int j=1;j<rec[i].p;j++)
				rec[m++]=rec[i];
		sort(rec,rec+m,cmp);
		for (int i=0;i<m;i++)
			for (int j=i+1;j<m;j++)
			{
				if (rec[i].e<rec[j].s) break;
				if (calc(rec[i].s,rec[i].e)+calc(rec[j].s,rec[j].e)<calc(rec[i].s,rec[j].e)+calc(rec[j].s,rec[i].e))
					swap(rec[i].e,rec[j].e);
			}
		for (int i=0;i<m;i++) 
			ans+=calc(rec[i].s,rec[i].e);
		ans-=total;
		printf("Case #%d: %I64d\n",t,ans);
	}
	return 0;
}