#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<ctype.h>
using namespace std;

#define X first
#define Y second
typedef long long ll;
typedef pair<int,int> Pi;

int chk[110][505];
int w, h, b;
int xx[4]={0,-1,0,1};
int yy[4]={-1,0,1,0};
int dfs(int x,int y,int t){
	if(y == h-1)return 1;
	int i;
	chk[x][y] = 0;
	int now = (t+3)%4;
	for(i=0;i<4;i++){
		int to = (now + i) % 4;
		if(x+xx[to] >= 0 && y+yy[to] >= 0 && chk[x+xx[to]][y+yy[to]] && dfs(x+xx[to],y+yy[to],to))break;
	}
	return i!=4;
}

int flow(){
	int i;
	for(i=0;i<w;i++)if(chk[i][0] && dfs(i,0,2))return 1;
	return 0;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int tt=1;tt<=Tc;tt++){
		printf("Case #%d: ", tt);
		memset(chk, 0, sizeof chk);
		scanf("%d%d%d",&w,&h,&b);
		for(int j=0;j<w;j++)for(int k=0;k<h;k++)chk[j][k] = 1;
		int i;
		for(i=1;i<=b;i++){
			int x0, y0, x1, y1;
			scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
			int j, k;
			for(j=x0;j<=x1;j++){
				for(k=y0;k<=y1;k++)chk[j][k] = 0;
			}
		}
		int ans = 0;
		while(flow()){
			ans++;
		}
		printf("%d\n",ans);
	}
	return 0;
}
