#include <vector>
#include <map>
//#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define sz(a) (int)(a.size())
#define len(a) (int)(a.length())
#define pb push_back
#define mp make_pair
#define fi first
#define se second

char a[105][105];
int d[105][105][4];
char our[]={'<','>','^','v'};

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<cas++<<": ";
		memset(d,0,sizeof(d));
		int r,c;
		cin>>r>>c;
		for(int i=0;i<r;++i)
			cin>>a[i];
		queue<pair<int,int> > q;
		for(int i=0;i<r;++i)
			q.push(mp(i,0));
		while(!q.empty())
		{
			pair<int,int> h=q.front(); q.pop();
			if(a[h.fi][h.se]!='.')
			{
				d[h.fi][h.se][0]=1;
			}
			else if(h.se<c-1)
			{
				q.push(mp(h.fi,h.se+1));
			}
		}
		while(!q.empty()) q.pop();
		for(int i=0;i<r;++i)
			q.push(mp(i,c-1));
		while(!q.empty())
		{
			pair<int,int> h=q.front(); q.pop();
			if(a[h.fi][h.se]!='.')
			{
				d[h.fi][h.se][1]=1;
			}
			else if(h.se>0)
			{
				q.push(mp(h.fi,h.se-1));
			}
		}
		while(!q.empty()) q.pop();
		for(int i=0;i<c;++i)
			q.push(mp(0,i));
		while(!q.empty())
		{
			pair<int,int> h=q.front(); q.pop();
			if(a[h.fi][h.se]!='.')
			{
				d[h.fi][h.se][2]=1;
			}
			else if(h.fi<r-1)
			{
				q.push(mp(h.fi+1,h.se));
			}
		}
		while(!q.empty()) q.pop();
		for(int i=0;i<c;++i)
			q.push(mp(r-1,i));
		while(!q.empty())
		{
			pair<int,int> h=q.front(); q.pop();
			if(a[h.fi][h.se]!='.')
			{
				d[h.fi][h.se][3]=1;
			}
			else if(h.fi>0)
			{
				q.push(mp(h.fi-1,h.se));
			}
		}
		while(!q.empty()) q.pop();
		int cnt=0;
		bool impossible=false;
		for(int i=0;i<r;++i)
			for(int j=0;j<c;++j)
				if(a[i][j]!='.')
				{
					for(int k=0;k<4;++k)
						if(d[i][j][k]==1&&a[i][j]==our[k])
						{
							bool exists=false;
							for(int p=0;p<4;++p)
								if(p!=k&&!d[i][j][p])
									exists=true;
							if(!exists) impossible=true;
							++cnt;
						}
				}
		if(impossible)
		{
			cout<<"IMPOSSIBLE\n";
		}
		else
		{
			cout<<cnt<<'\n';
		}
	}

	return 0;
}