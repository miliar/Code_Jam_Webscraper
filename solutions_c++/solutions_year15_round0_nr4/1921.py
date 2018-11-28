#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<cstdlib>
#include<fstream>
#include<ctime>
#include<string>
using namespace std;
#define ll long long
#define mxn 100010
#define mxe 200010
#define inf 0x3f3f3f3f
//#define mp make_pair
#define pii pair<int,int>

int a[10][10][10];

int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	memset(a,0,sizeof(a));
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
		{
			a[1][i][j]=1;
			a[i][i][j]=a[i][j][i]=1;
		}
	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
			a[4][i][j]=0;
	for(int i=1;i<=4;i++)
		a[2][4][i]=a[2][i][4]=1;
	a[3][1][3]=a[3][3][1]=0;
	a[4][3][4]=a[4][4][3]=a[4][4][4]=1;
/*	for(int i=1;i<=4;i++)
		for(int j=1;j<=4;j++)
			for(int k=1;k<=4;k++)
				printf("a[%d][%d][%d]=%d\n",i,j,k,a[i][j][k]);
*/	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(a[x][r][c])
			printf("Case #%d: GABRIEL\n",t);
		else
			printf("Case #%d: RICHARD\n",t);
	}
	return 0;
}





	










		


				





						




