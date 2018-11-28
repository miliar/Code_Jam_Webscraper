#include<bits/stdc++.h>
using namespace std;

const int dx[]={-1,0,1,0},
		dy[]={0,1,0,-1};
char a[128][128];
const char* dd="^>v<";
int n,m;
int main(){
	int T;
	scanf("%d",&T);
	for(int ti=1;ti<=T;++ti){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)scanf("%s",a[i]);
		int c=0;
		bool ok=true;
		for(int i=0;i<n && ok;++i)
			for(int j=0;j<m && ok;++j)if(a[i][j]!='.'){
				int k=strchr(dd,a[i][j])-dd,
					dx=::dx[k],dy=::dy[k],x=i,y=j;
				bool e=false;
				do{
					x+=dx;y+=dy;
					if(x<0||y<0||x>=n||y>=m)break;
					e= (a[x][y]!='.');
				}while(!e);
				if(e)continue;
				for(int tm=3;tm-- && !e;){
					k=k+1&3;
					dx=::dx[k],dy=::dy[k];
					x=i,y=j;
					do{
						x+=dx;y+=dy;
						if(x<0||y<0||x>=n||y>=m)break;
						e= (a[x][y]!='.');
					}while(!e);
				}
				ok=e;++c;
			}
		printf("Case #%d: ",ti);
		if(!ok)puts("IMPOSSIBLE");
		else printf("%d\n",c);
	}
}
