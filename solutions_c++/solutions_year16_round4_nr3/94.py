#include<stdio.h>
#include<algorithm>
int tcn,tc;
int n,m;
int a[100];
char map[100][100];
int search(int p){
	int x,y,vx,vy,t;
	if(p<m){
		x=0;
		y=p;
		vx=1;
		vy=0;
	}
	else if(p<n+m){
		x=p-m;
		y=m-1;
		vx=0;
		vy=-1;
	}
	else if(p<n+m*2){
		x=n-1;
		y=n+m*2-1-p;
		vx=-1;
		vy=0;
	}
	else{
		x=2*n+2*m-1-p;
		y=0;
		vx=0;
		vy=1;
	}
	while(x>=0&&y>=0&&x<n&&y<m){
		if(map[x][y]=='/'){
			t=-vx;
			vx=-vy;
			vy=t;
		}
		else{
			t=vx;
			vx=vy;
			vy=t;
		}
		x+=vx;
		y+=vy;
	}
	if(x<0){
		return y;
	}
	else if(y>=m){
		return x+m;
	}
	else if(x>=n){
		return n+m*2-1-y;
	}
	else{
		return 2*n+2*m-1-x;
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,ta,tb;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d%d",&n,&m);
		for(i=0;i<n+m;i++){
			scanf("%d%d",&ta,&tb);
			ta--;
			tb--;
			a[ta]=tb;
			a[tb]=ta;
		}
		printf("Case #%d:\n",tc);
		for(i=0;i<(1<<(n*m));i++){
			for(j=0;j<n;j++){
				for(k=0;k<m;k++){
					if(((i>>(j*m+k))&1)==0){
						map[j][k]='/';
					}
					else{
						map[j][k]='\\';
					}
				}
				map[j][m]=0;
			}
			for(j=0;j<(n+m)*2;j++){
				if(search(j)!=a[j]){
					break;
				}
			}
			if(j==(n+m)*2){
				for(j=0;j<n;j++){
					puts(map[j]);
				}
				break;
			}
		}
		if(i==(1<<(n*m)))puts("IMPOSSIBLE");
	}
	return 0;
}