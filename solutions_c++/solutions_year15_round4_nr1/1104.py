#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
string g[110];
int n,m;
pair<int,int> mv[256];
bool check(int i,int j,pair<int,int> nmv)
{
	i+=nmv.first;
	j+=nmv.second;
	while(i>=0&&j>=0&&i<n&&j<m)
	{
		if(g[i][j]!='.')
			return 1;
		i+=nmv.first;
		j+=nmv.second;
	}
	return 0;
}
int main()
{
	mv['^']={-1,0};
	mv['v']={1,0};
	mv['>']={0,1};
	mv['<']={0,-1};	
	
	int T,no=1;
	cin>>T;
	while(no<=T)
	{
		cin>>n>>m;
		for(int i=0;i<n;i++)
			cin>>g[i];
		int ans=0;
		for(int i=0;i<n&&ans!=-1;i++)
			for(int j=0;j<m;j++)
			{
				if(g[i][j]=='.')continue;
				if(!check(i,j,mv[g[i][j]]))
				{
					ans++;
					char four[4]={'^','v','>','<'};
					bool ok=0;
					for(int k=0;k<4;k++)
					{
						if(check(i,j,mv[four[k]]))
						{
							ok=1;
							break;
						}
					}
					if(!ok)
					{
						ans=-1;
						break;
					}
				}
			}
		if(ans==-1)
			printf("Case #%d: IMPOSSIBLE\n",no++);
		else
			printf("Case #%d: %d\n",no++,ans);
	}
}
