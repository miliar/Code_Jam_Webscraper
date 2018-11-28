#include <bits/stdc++.h>

using namespace std;

int vis[50][50];
int dx[]={0 ,0,1 ,1,1,-1,-1,-1};
int dy[]={-1,1,-1,0,1,-1,0, 1};
int r,c,m;
int in(int x,int y)
{
	
	if(x<0 || y<0) return 0;
	if(x>=r||y>=c) return 0;
	return 1;
}
char s[50][50];
void create_grid()
{
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			int z=0;
			
			if(s[i][j]!='*')
			{
				for(int k=0;k<8;k++)
				{
					int tx=i+dx[k];
					int ty=j+dy[k];
					if(!in(tx,ty)) continue;
					if(s[tx][ty]=='*') z++;
				}
				s[i][j]=char('0'+z);
			}
			
		}
	}
}
int solve()
{
	
	for(int i=0;i<r;i++)
	{
		for(int j=0;j<c;j++)
		{
			if(s[i][j]=='*') continue;
			queue<pair<int,int> > q;
			q.push(make_pair(i,j));
			memset(vis,0,sizeof(vis));
			vis[i][j]=1;
			while(!q.empty())
			{
				int x=q.front().first;
				int y=q.front().second;
				q.pop();
				if(!in(x,y)) continue;
				//if(vis[x][y]) continue;
				if(s[x][y]!='0') continue;
				
				for(int k=0;k<8;k++)
				{
					int tx=x+dx[k];
					int ty=y+dy[k];
					if(!in(tx,ty)) continue;
					if(s[tx][ty]=='*') continue;
					if(vis[tx][ty]) continue;
					vis[tx][ty]=1;
					if(s[tx][ty]!='0')
					{
						
						continue;
					}
					
					q.push(make_pair(tx,ty));
				}
			}
			int co=0;
			for(int x=0;x<r;x++)
			{
				for(int y=0;y<c;y++)
				{
					co+=vis[x][y];
				}
			}
			
			if(co==r*c-m)
			{
				//cout<<"Yeah"<<endl;
				for(int x=0;x<r;x++)
				{
					for(int y=0;y<c;y++)
					{
						if(x==i && y==j)
						{
							cout<<"c"; continue;
						}
						if(s[x][y]!='*' ) s[x][y]='.';
						cout<<s[x][y];
						
						
					}
					cout<<endl;
				}
				
				return 1;
			}
		}
	}
	return 0;
	cout<<"Impossible"<<endl;
}
int main()
{
  freopen("in3.in","r",stdin);
  freopen("out3.out","w",stdout);
  int tc;
  cin>>tc;
  for(int t=1;t<=tc;t++)
  {
	  
	  cout<<"Case #"<<t<<":"<<endl;
	  memset(vis,0,sizeof(vis));
	  cin>>r>>c>>m;
	  int z=1;
	  string g(r*c,'0');
	  for(int i=0;i<(1<<(r*c));i++)
	  {
		  int co=0;
		 // cout<<i<<endl;
		  g= string(r*c,'0');
		  for(int j=0;j<(r*c);j++)
		  {
			  if(i & (1<<j))
			  {
				  co++;
				  g[j]='*';
			  }
		  }
		  if(co!=m)
		  {
			  continue;
		  }
		  //cout<<g.substr(0,r*c)<<endl;
		  for(int j=0;j<r*c;j++)
		  {
			  s[j/c][j%c]=g[j];
		  }
		  for(int i=0;i<r;i++)
		  {
			  for(int j=0;j<c;j++)
			  {
				  //cout<<s[i][j];
			  }
			  //cout<<endl;
		  }
		  //cout<<endl;
		  create_grid();
		  if(solve())
		  {
			  z=0;
			  break;
		  }
	  }
	  if(z)
	  {
		  cout<<"Impossible"<<endl;
	  }
	  
	  
	 
	  
  }	
  return 0;
}
