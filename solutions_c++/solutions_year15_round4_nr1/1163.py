#include <iostream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <string.h>
#include <cmath>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef long long ll;
int R,C;
char g[100][101];
int dr[4]={-1,1,0,0};
int dc[4]={0,0,-1,1};
char D[128];
int vis[100][100], vs;
bool check(int r, int c){
	int d = D[g[r][c]];
	while (true){
		r += dr[d];
		c += dc[d];
		if (!(r<R && c<C && r >= 0 && c >= 0))
			return true;
		if (g[r][c] != '.')
			break;
	}
	return false;
}
int main()
{
	freopen("src.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	D['^'] = 0; D['v'] = 1; D['<'] = 2; D['>'] = 3;
	int T;
	scanf("%d",&T);
	for (int Z = 1; Z <= T; ++Z){
		printf("Case #%d: ", Z);
		scanf("%d%d",&R,&C);
		for(int i=0;i<R;++i)
			scanf("%s",g[i]);
		int ans = 0;
		for (int i = 0; i<R; ++i)
			for(int j=0;j<C;++j)
				if(g[i][j]!='.')
					if(check(i,j)){
						char res=-1;
						for (int k = i - 1; res == -1 && k >= 0; --k)
						if (g[k][j] != '.')
							res = '^';
						for (int k = i +1; res == -1 && k <R; ++k)
						if (g[k][j] != '.')
							res = 'v';
						for (int k = j + 1; res == -1 && k <C; ++k)
						if (g[i][k] != '.')
							res = '>';
						for (int k = j - 1; res == -1 && k >= 0; --k)
						if (g[i][k] != '.')
							res = '<';
						if(res==-1){
							i=R;
							j=C;
							ans=-1;
						}else{
							g[i][j]=res;
							++ans;
						}
					}
		if(ans==-1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}
	return 0;
}