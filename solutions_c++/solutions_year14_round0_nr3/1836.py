#include <bits/stdc++.h>

using namespace std;
typedef pair<int,int> pii;

bool inrange(int i,int j,int r ,int c)
{
	if(i<r&&i>=0&&j<c&&j>=0)
	return true;
	return false;
}

int g[5][5];
int vis[5][5];
int R,C,M;

int main()
{
	int T;
	cin>>T;
	int caseno=0;
	while(T--)
	{
		caseno++;
		printf("Case #%d:\n",caseno);
		cin>>R>>C;
		cin>>M;
		int x[]={1,1,-1,-1,0,0,-1,1};
		int y[]={1,0,-1,0,1,-1,1,-1};
		int N=R*C;
		int flag=0;
		for(int i=0;i<(1<<N);i++)
		{
			int m=0;
			for(int k=0;k<R;k++)
			{
				for(int l=0;l<C;l++)
				{
						g[k][l]=(((i)&(1<<(k*C+l)))?1:0);
						if(g[k][l]==1)
						m++;
				}
			}
			if(m!=M)
			continue;
			memset(vis,0,sizeof(vis));
			for(int k=0;k<R;k++)
			{
				flag=0;
				for(int l=0;l<C;l++)
				{
					//cout<<"Second Stage\n";
					memset(vis,0,sizeof(vis));
					queue<pii> q;
					if(g[k][l]==0)
					q.push(pii(k,l));
					else
					continue;
					int cnt=0;
					vis[k][l]=1;
					while(!q.empty())
					{
						pii p=q.front();
						q.pop();
						int a=p.first;
						int b=p.second;
						int count=0;
						for(int j=0;j<8;j++)
						{
							int X=a+x[j];int Y=b+y[j];
							if(inrange(X,Y,R,C))
							{
								if(g[X][Y]==1)
								count++;	
							}
						}
						if(count==0)
						{
							for(int j=0;j<8;j++)
							{
								int X=a+x[j];int Y=b+y[j];
								if(inrange(X,Y,R,C))
								{
									if(!vis[X][Y]&&!g[X][Y])
									{
										q.push(pii(X,Y));
										vis[X][Y]=1;
									}	
								}
							}
						}
					}
					flag=1;
					for(int u=0;u<R;u++)
					{
						for(int v=0;v<C;v++)
						{
							if(!vis[u][v]&&!g[u][v])
							flag=0;
						}
					}
					if(flag)
					{
						for(int u=0;u<R;u++)
						{
							for(int v=0;v<C;v++)
							{
								if(g[u][v])
								cout<<"*";
								else
								{
									if(u==k&&v==l)
									cout<<"c";
									else
									cout<<".";
								}
							}
							cout<<endl;
						}
						break;	
					}
					
				}
				if(flag)
				break;
			}
			if(flag)
			break;
			/*
			for(int k=0;k<R;k++)
			{
				for(int l=0;l<C;l++)
				{
					int count=0;
					for(int j=0;j<8;j++)
					{
						int X=k+x[j];int Y=l+y[j];
						if(inrange(X,Y,R,C))
						{
							if(g[X][Y]==1)
							count++;	
						}
					}
					if(count==0)
					{
						vis[k][l]=2;
						for(int j=0;j<8;j++)
						{
							int X=k+x[j];int Y=l+y[j];
							if(inrange(X,Y,R,C))
							{
								if(vis[X][Y]==0)
								vis[X][Y]=1;
							}
						}
					}
					
				}
			}
			flag=1;
			for(int u=0;u<R;u++)
			{
				for(int v=0;v<C;v++)
				{
					if(!vis[u][v]&&!g[u][v])
					flag=0;
				}
			}
			int cc=0;
			if(flag)
			{
				for(int u=0;u<R;u++)
				{
					for(int v=0;v<C;v++)
					{
						if(g[u][v])
						cout<<"*";
						else
						{
							if(vis[u][v]==2&&!cc)
							printf("c"),cc=1;
							else
							printf(".");
						}
					}
					printf("\n");
				}
				break;
			}*/
		}
		if(!flag)
		cout<<"Impossible"<<endl;
	}
}
