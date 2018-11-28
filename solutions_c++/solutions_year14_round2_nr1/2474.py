#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,i,j,k;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		char a[1000][1000]={{0}};
		for(i=0;i<n;i++)
		scanf("%s",a[i]);
		vector< pair<char,int> >v[110];
		for(i=0;i<n;i++)
		{
			char c=a[i][0];
			int k=1;
//			b[i][0]=a[i][0];
			v[i].push_back(make_pair(a[i][0],1));
			for(j=1;a[i][j];j++)
			{
				if(c!=a[i][j])
				{
					v[i].push_back(make_pair(a[i][j],1));
					c=a[i][j];
				}
				else
				{
					v[i][v[i].size()-1].second++;
				}
			}
		}
		int x=v[0].size(),y,z,sum=0,p,q,r;
		int f=0;
		for(i=0;i<n;i++)
		if(x!=v[i].size())
		f=1;
		for(j=0;j<v[0].size();j++)
		{
			x=0;
			for(i=0;i<n-1;i++)
			{
				if(v[i][j].first!=v[i+1][j].first)
				f=1;
				else
				x+=v[i][j].second;
			}
			if(f==1)
			break;
			x+=v[n-1][j].second;
			x=x/n;
			y=x-1;
			z=x+1;p=q=r=0;
			for(i=0;i<n;i++)
			{
				p+=abs(x-v[i][j].second);
				q+=abs(y-v[i][j].second);
				r+=abs(z-v[i][j].second);
			}
			sum+=min(p,min(q,r));
		}
		if(f==1)
		printf("Case #%d: Fegla Won\n",k);
		else
		printf("Case #%d: %d\n",k,sum);
	}
	return 0;
}
