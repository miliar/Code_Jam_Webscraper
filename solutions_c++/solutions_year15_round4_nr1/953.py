#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
using std::vector;
using std::pair;
using std::make_pair;
using std::sort;
char s[105][105];
int vis[105][105]; 
int main(void){
	int t,hh;
	scanf("%d",&t);
	for(hh=1;hh<=t;hh++){
		int n,m;
		scanf("%d%d",&n,&m);
		int i,j,k;
		char ss[105];
		for(i=0;i<n;i++){
		  scanf("%s",ss);
		  for(j=0;j<m;j++)
		    s[i][j]=ss[j],vis[i][j]=0;
		}
		int ans=0;
		for(i=0;i<n;i++)
		  for(j=0;j<m;j++){
		  	  if(s[i][j]=='.') continue;
		  	  if(vis[i][j]) continue;
		  	  int nx=i,ny=j,dx=0,dy=0,px,py;
		  	  for(;;){
		  //	  	printf("%d %d\n",nx,ny);
		  	  	if(s[nx][ny]!='.'){
		  	  		vis[nx][ny]=1;
		  	  		px=nx,py=ny;
		  	  	} 
		  //	  	printf("%d %d %d %d\n",i,j,nx,ny);
		  	  	if(s[nx][ny]=='>') dx=0,dy=1;
		  	  	else if(s[nx][ny]=='^') dx=-1,dy=0;
		  	  	else if(s[nx][ny]=='<') dx=0,dy=-1;
		  	  	else if(s[nx][ny]=='v') dx=1,dy=0;
		  	  	nx+=dx,ny+=dy;
		  	  	int ok=1;
		  	  	if(nx<0||nx>=n||ny<0||ny>=m){
		  	  		ok=0;
		  	  	//	printf("%d %d %d\n",i,j,ans);
		  	  		for(k=px-1;k>=0&&!ok;k--){
						if(s[k][py]!='.'){
		  	  				ans++;
		  	  				ok=1;
		  	  				break;
						} 
		  	  		}
		  	  		for(k=px+1;k<n&&!ok;k++){
		  	  			if(s[k][py]!='.'){
		  	  				ans++;
		  	  				ok=1;
		  	  				break;
						} 
		  	  		}
		  	  		for(k=py-1;k>=0&&!ok;k--){
		  	  			if(s[px][k]!='.'){
		  	  				ans++;
		  	  				ok=1;
		  	  				break;
						} 
		  	  		}
		  	  		for(k=py+1;k<m&&!ok;k++){
		  	  			if(s[px][k]!='.'){
		  	  				ans++;
		  	  				ok=1;
		  	  				break;
						} 
		  	  		}
		  	  		if(!ok) ans=-1;
		  	  		else break;
		  	  	}
		  	  	if(vis[nx][ny]) break;
		  	  	if(ans==-1) break;
		  	  }
		      if(ans==-1) break;
		  	
		  }
		if(ans==-1) printf("Case #%d: IMPOSSIBLE\n",hh);
		else printf("Case #%d: %d\n",hh,ans);
		
	}
	return 0;
}

