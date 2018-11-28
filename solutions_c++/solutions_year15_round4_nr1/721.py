#include<set>
#include<map>
#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<queue>
#include<math.h>
using namespace std;
char ch[100][101];
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};//'v','^','>','<'
int n,m;
bool go(int x,int y,int d){
	if(x<0||y<0||x>=n||y>=m)return false;
	if(ch[x][y]!='.')return true;
	return go(x+dx[d],y+dy[d],d);
}
int main(){
	int ca;
	scanf("%d",&ca);
	for(int cas=1;cas<=ca;cas++){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			scanf("%s",ch[i]);
		int cnt=0;
		bool f=true;
		for(int i=0;i<n&&f;i++)
			for(int j=0;j<m&&f;j++){
				int d;
				if(ch[i][j]=='>')d=0;
				else if(ch[i][j]=='<')d=1;
				else if(ch[i][j]=='v')d=2;
				else if(ch[i][j]=='^')d=3;
				else continue;
				ch[i][j]='.';
				if(go(i,j,d)){
					ch[i][j]='v';
					continue;
				}
				for(int dd=0;;dd++){
					if(dd==d)continue;
					if(dd==4){
						f=false;
						break;
					}
					if(go(i,j,dd)){
						cnt++;
						ch[i][j]='v';
						break;
					}
				}
			}
		printf("Case #%d: ",cas);
		if(!f)printf("IMPOSSIBLE\n");
		else printf("%d\n",cnt);
	}

}
