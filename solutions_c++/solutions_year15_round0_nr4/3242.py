#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<queue>
#include<map>
#include<memory.h>
using namespace std;
bool vis[5][5][5];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	vis[2][1][1]=1,vis[2][3][1]=1,vis[2][1][3]=1,vis[2][3][3]=1;
	vis[3][1][1]=1,vis[3][1][2]=1,vis[3][1][3]=1,vis[3][2][1]=1;
	vis[3][2][2]=1,vis[3][2][4]=1,vis[3][3][1]=1,vis[3][4][1]=1;
	vis[3][4][2]=1,vis[3][1][4]=1,vis[3][4][4]=1;
	vis[4][1][1]=1,vis[4][1][2]=1,vis[4][1][3]=1,vis[4][1][4]=1;
	vis[4][2][1]=1,vis[4][2][2]=1,vis[4][2][3]=1,vis[4][2][4]=1;
	vis[4][3][1]=1,vis[4][3][2]=1,vis[4][4][1]=1,vis[4][4][2]=1;
	vis[4][3][3]=1;
	
	int x,r,c,t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>x>>r>>c;
		string ans;
		
		if(vis[x][r][c]==1)
			ans="RICHARD";
		else
			ans="GABRIEL";
		
		cout<<"Case #"<<k<<": "<<ans<<endl;
	
	}
}

