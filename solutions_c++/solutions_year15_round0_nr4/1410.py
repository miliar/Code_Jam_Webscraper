#include<iostream> 
#include<string> 
#include<queue> 
#include<algorithm> 
#include<cstdio> 
#include<vector> 
#include<queue> 
#include<climits> 
#include<cstring> 
#include<ctime>
#include<cstdlib>
using namespace std; 

bool ans[5][5][5];

void init()
{
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
			ans[1][i][j]=true;

	for(int i=1;i<=4;i++)
	{
		for(int j=1;j<=4;j++)
		{
			if((i*j)%2==0) ans[2][i][j]=true;
			else ans[2][i][j]=false;
		}
	}

	ans[3][1][1]=false;
	ans[3][1][2]=false;
	ans[3][1][3]=false;
	ans[3][1][4]=false;
	ans[3][2][1]=false;
	ans[3][2][2]=false;
	ans[3][2][3]=true;
	ans[3][2][4]=false;
	ans[3][3][1]=false;
	ans[3][3][2]=true;
	ans[3][3][3]=true;
	ans[3][3][4]=true;
	ans[3][4][1]=false;
	ans[3][4][2]=false;
	ans[3][4][3]=true;
	ans[3][4][4]=false;

	ans[4][1][1]=false;
	ans[4][1][2]=false;
	ans[4][1][3]=false;
	ans[4][1][4]=false;
	ans[4][2][1]=false;
	ans[4][2][2]=false;
	ans[4][2][3]=false;
	ans[4][2][4]=false;
	ans[4][3][1]=false;
	ans[4][3][2]=false;
	ans[4][3][3]=false;
	ans[4][3][4]=true;
	ans[4][4][1]=false;
	ans[4][4][2]=false;
	ans[4][4][3]=true;
	ans[4][4][4]=true;

}
int main()
{
	freopen("d://output.txt","w",stdout);
	freopen("d://D-small-attempt0.in","r",stdin);
	init();
	int Kase;
	scanf("%d",&Kase);
	for(int Case=1;Case<=Kase;Case++)
	{
		printf("Case #%d: ",Case);
		int a,b,c;
		scanf("%d%d%d",&a,&b,&c);
		if(ans[a][b][c]) printf("GABRIEL\n");
		else printf("RICHARD\n");
	}
}

