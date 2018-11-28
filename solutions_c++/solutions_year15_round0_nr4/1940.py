#include<cstdio>
#include<cstring>
#include<algorithm>
#define fou(i,j,k) for (int i=j;i<=k;i++)
#define fod(i,j,k) for (int i=j;i>=k;i--)
using namespace std;

typedef long long LL;

bool f[6][6][6];

void solve()
{
	fou(i,1,4)
		fou(j,1,4){
			f[1][i][j]=false;
			if (i%2==0 || j%2==0) f[2][i][j]=false;
			else f[2][i][j]=true;
			f[3][i][j]=true;
			f[4][i][j]=true;
		}
	f[3][3][3]=f[3][2][3]=f[3][3][2]=f[3][4][3]=f[3][3][4]=false;
	f[4][4][4]=f[4][3][4]=f[4][4][3]=false;
}

int main()
{
	int T,x,r,c;
	solve();
	scanf("%d",&T);
	fou(i,1,T){
		printf("Case #%d: ",i);
		scanf("%d%d%d",&x,&r,&c);
		if (f[x][r][c]) printf("RICHARD\n");
		else printf("GABRIEL\n");
	}
	return 0;
}
