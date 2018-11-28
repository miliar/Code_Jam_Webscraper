#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
bool check(int c,int n){
	int cnt=0;
	while(c){
		cnt+=(c&1);
		c>>=1;
	}
	return cnt==n;
}

int R,C,N;
bool isin(int x,int y){
	return x>=0&&x<R&&y>=0&&y<C;
}
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
int mp[20][20];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d %d %d",&R,&C,&N);
		int A=R*C;
		int ans=10000;
		for(int i=0;i<(1<<A);i++){
			if(check(i,N)){
				memset(mp,0,sizeof(mp));
				for(int j=0;j<A;j++){
					if((i>>j)&1){
						mp[j/C][j%C]=1;
					}
				}
				int cnt=0;
				for(int r=0;r<R;r++){
					for(int c=0;c<C;c++){
						if(mp[r][c]==0)continue;
						for(int k=0;k<4;k++){
							int tx=r+dx[k],ty=c+dy[k];
							if(isin(tx,ty)&&mp[tx][ty]){
								cnt++;
							}
						}
					}
				}
				ans=min(ans,cnt);
			}
		}
		printf("Case #%d: %d\n",t,ans/2);
	}
	return 0;
}
