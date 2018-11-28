#include <bits/stdc++.h>
using namespace std;
bool mycomp(pair<int,int> a,pair<int,int> b)
{
	if(a.first>b.first)
		return true;
	return false;
}
void find(vector <pair <int,int> >&a, int lim)
{
	int i,v,j;
	v = lim==a.size()?0:a[lim].first;

	for(i=a[0].first;i>v;i--)
	{
		j=0;
		if(lim%2==1)
		{
			printf("%c ",a[0].second+'A');
			a[0].first--;
			j=1;
		}	
		for(;j<lim;j+=2)
		{
			printf("%c%c ",a[j].second+'A',a[j+1].second+'A');
			a[j].first--;
			a[j+1].first--;
		}
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int t,T,n,i,j;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		vector < pair<int,int> >p(26);
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&p[i].first);
			p[i].second = i;
		}	
		sort(p.begin(), p.end(),mycomp);
		printf("Case #%d: ",t);
		for(i=1;i<n;i++)
		{
			if(p[i-1].first==p[i].first)
				continue;
			find(p,i);
		}
		find(p,n);
		printf("\n");
	}
	return 0;
}
