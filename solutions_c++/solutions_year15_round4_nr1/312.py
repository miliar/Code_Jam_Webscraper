#include <bits/stdc++.h>
using namespace std;

char g[105][105];
int R,C;
int dx[]={-1,0,0,1};
int dy[]={0,1,-1,0};
bool bound(int x,int y){
	if(x >= 0 && x < R && y >=0 && y <C)return true;
	else return false;
}
int getDir(char c){
	if(c == '<' )return 2;
	else if(c == '^')return 0;
	else if(c == 'v')return 3;
	else return 1;
}
void solve(){
	scanf("%d%d",&R,&C);
	for(int i = 0; i < R; i++)scanf("%s",g[i]);
	bool flag = 1;
	int cnt = 0,ans = 0;
	for(int i = 0; i  < R; i++){
		for(int j = 0 ; j < C; j++){
			if(g[i][j] == '.')continue;
			int ok = 4;
			ans++;
			for(int k = 0; k < 4; k++){
				int st = 1;
				for(int x=i + st*dx[k],y=j + st*dy[k]; bound(x,y); ++st,x = i + st*dx[k],y = j + st*dy[k]){
					if(g[x][y] != '.'){
						if(getDir(g[i][j]) == k)ans--;
					//	printf("fuck %d %d  x y = %d %d\n",getDir(g[i][j]),k,x,y);
						ok--;
						break;
					}
				}
			}
			if(ok == 4){
				flag = 0;
				break;
			}
		}
	}
	if(flag)printf("%d\n",ans);
	else puts("IMPOSSIBLE");
}
int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 0; cas < T; cas++){
		printf("Case #%d: ",cas+1);
		solve();
	}
	return 0;
}
