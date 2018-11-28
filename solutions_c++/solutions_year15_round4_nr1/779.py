#include<iostream>
#include<fstream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<vector>
#include<functional>
#include<string>

#define INF 1000000007
#define pb push_back
#define mp make_pair
#define ll long long
#define rep(i,k) for(int i=G.start[k];i!=INF;i=G.next[i])

using namespace std;

char M[105][105];
int Up[105][105],Down[105][105],Left[105][105],Right[105][105];

int main()
{
freopen("t.in","r",stdin);
freopen("t.out","w",stdout);
	ios::sync_with_stdio(false);
	
	int T;
    cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		memset(Up,0,sizeof(Up));
		memset(Down,0,sizeof(Down));
		memset(Left,0,sizeof(Left));
		memset(Right,0,sizeof(Right));
		int R,C,ans=0;
		bool fg=0;
		cin>>R>>C;
		for(int i=1;i<=R;i++)
			for(int j=1;j<=C;j++)
				cin>>M[i][j];
		for(int i=1;i<=R;i++)
			for(int j=1;j<=C;j++)
				if(M[i][j]!='.')
				{
					Up[i][j]=Up[i-1][j]+1;
					Left[i][j]=Left[i][j-1]+1;
				}
				else
				{
					Up[i][j]=Up[i-1][j];
					Left[i][j]=Left[i][j-1];
				}
		for(int i=R;i>=1;i--)
			for(int j=C;j>=1;j--)
				if(M[i][j]!='.')
				{
					Down[i][j]=Down[i+1][j]+1;
					Right[i][j]=Right[i][j+1]+1;
				}
				else
				{
					Down[i][j]=Down[i+1][j];
					Right[i][j]=Right[i][j+1];
				}
		for(int i=R;i>=1;i--)
			for(int j=C;j>=1;j--)
				if(M[i][j]!='.')
				{
					Up[i][j]--;
					Down[i][j]--;
					Left[i][j]--;
					Right[i][j]--;
				}
		for(int i=1;i<=R;i++)
			for(int j=1;j<=C;j++)
			{
				if(M[i][j]=='.')continue;
				if((Up[i][j]||Down[i][j]||Left[i][j]||Right[i][j])==0)
				{
					fg=true;break;
				}
				if(M[i][j]=='^')
					if(!Up[i][j])ans++;
				if(M[i][j]=='<')
					if(!Left[i][j])ans++;
				if(M[i][j]=='>')
					if(!Right[i][j])ans++;
				if(M[i][j]=='v')
					if(!Down[i][j])ans++;
			}
		
		if(!fg)cout<<"Case #"<<cas<<": "<<ans<<endl;
		else cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}
