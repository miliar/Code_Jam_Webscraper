#include <bits/stdc++.h>

using namespace std;

int n,m;
char ch[110][110];
int di[4]={-1,0,1,0};
int dj[4]={0,1,0,-1};

int dfs(int x,int y,int k){
	if (x<0 || x>=n || y<0 || y>=m) return 0;
	if (ch[x][y]!='.') return 1;
		else return dfs(x+di[k],y+dj[k],k);
}

int main(){
	int T;
	scanf("%d",&T);
	for (int ti=1;ti<=T;ti++){
		printf("Case #%d: ",ti);
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) scanf("%s",ch[i]);
		int flag=1,ans=0;
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (ch[i][j]!='.'){
					int k=0;
					if (ch[i][j]=='^') k=0;
					if (ch[i][j]=='>') k=1;
					if (ch[i][j]=='v') k=2;
					if (ch[i][j]=='<') k=3;
					int now=0;
					for (int p=0;p<4;p++){
						int bo=dfs(i+di[p],j+dj[p],p);
						now+=bo;
						if (p==k && bo) now-=10;
					}
					if (now>0) ans++;
					if (now==0) flag=0;
			}
		if (flag) printf("%d\n",ans);
			else printf("IMPOSSIBLE\n");
	}
	return 0;
}
