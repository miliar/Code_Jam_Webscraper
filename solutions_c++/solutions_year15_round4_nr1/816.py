#include<stdio.h>
char f[100][100];
int cnt[100][100];

int main(){
	int dn;
	scanf("%d",&dn);
	for(int di=0;di<dn;di++){
	int H,W;
	scanf("%d %d",&H,&W);
	int i,j;
	for(i=0;i<H;i++){
		for(j=0;j<W;j++){
			scanf(" %c",&f[i][j]);
			cnt[i][j]=0;
		}
	}
	int ans=0;
	for(i=0;i<W;i++){
		int y=0;
		while(y<H){
			if(f[y][i]!='.'){
				if(f[y][i]=='^')ans++;
				cnt[y][i]++;
				break;
			}
			y++;
		}
		y=H-1;
		while(y>=0){
			if(f[y][i]!='.'){
				if(f[y][i]=='v')ans++;
				cnt[y][i]++;
				break;
			}
			y--;
		}
	}
	for(i=0;i<H;i++){
		int x=0;
		while(x<W){
			if(f[i][x]!='.'){
				if(f[i][x]=='<')ans++;
				cnt[i][x]++;
				break;
			}
			x++;
		}
		x=W-1;
		while(x>=0){
			if(f[i][x]!='.'){
				if(f[i][x]=='>')ans++;
				cnt[i][x]++;
				break;
			}
			x--;
		}
	}
		printf("Case #%d: ",di+1);
		bool f=true;
		for(i=0;i<H;i++){
			for(j=0;j<W;j++){
				if(cnt[i][j]==4)f=false;
			}
		}
		if(f)printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}