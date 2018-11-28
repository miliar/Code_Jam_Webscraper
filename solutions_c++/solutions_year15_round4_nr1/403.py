#include<cstdio>
#define N 110
using namespace std;
char s[N][N];
int mx[4]={0,1,0,-1},my[4]={1,0,-1,0};
char dir[128];
int main(){
	int T,n,m,cs,d,i,j,k,x,y,ans;
	bool yes[4],wrong;
	dir['v']=1;
	dir['<']=2;
	dir['^']=3;
	dir['>']=0;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		ans=0;
		wrong=false;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%s",s[i]);
		}
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(s[i][j]!='.'){
					d=dir[s[i][j]];
					for(k=0;k<4;k++){
						yes[k]=false;
					}
					for(k=0;k<4;k++){
						x=i+mx[k];
						y=j+my[k];
						while(x>=0&&x<n&&y>=0&&y<m){
							if(s[x][y]!='.') yes[k]=true;
							x+=mx[k];
							y+=my[k];
						}
					}
					if(!yes[d]) ans++;
					if(!yes[0]&&!yes[1]&&!yes[2]&&!yes[3]) wrong=true;
				}
			}
		}
		if(wrong) printf("Case #%d: IMPOSSIBLE\n",cs);
		else printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}