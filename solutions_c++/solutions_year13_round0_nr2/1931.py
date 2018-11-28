#include<iostream>
#include<cstdio>
using namespace std;

int n,m,map[110][110];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,cas,c;
	bool cut,cuth,cutv,ans;
	memset(map,0,sizeof(map));
	cin>>cas;
	for(c=1;c<=cas;c++)
	{
		printf("Case #%d: ",c);
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				cin>>map[i][j];
		ans=1;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				cuth=1;cutv=1;
				for(k=1;k<=m;k++)
					if(map[i][j]<map[i][k])
					{
						cuth=0;
						break;
					}
				for(k=1;k<=n;k++)
					if(map[i][j]<map[k][j])
					{
						cutv=0;
						break;
					}
				if(cuth==1 || cutv==1) cut=1;
				else cut=0;
				if(cut==0) 
				{
					ans=0;
					break;
				}
			}
			if(ans==0)break;
		}
		if(ans==0) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}

				
	
	