#include <iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int N=100;
int Map[N][N];
int min(int a,int b){
	return a<b?a:b;
}
int max(int a,int b){
	return a<b?b:a;
}
void Swap(int &a,int &b){
	int x=a;
	a=b;
	b=x;
}
int R,C,n,ans;
bool vis[N][N];
void Next_xy(int &x,int &y){
	y++;
	if(y==C)
		x++,y=0;
}
void dfs(int no,int cx,int cy,int sum){
	if(sum>=ans)
		return;		
	if(no==0){	
		if(sum<ans)
			ans=sum;
		return;
	}
	if(cx==R)
		return;	
	int nx,ny;
	nx=cx,ny=cy;
	Next_xy(nx,ny);
	
	
	int temp=0;
	if(cx-1>=0&&vis[cx-1][cy])
		temp++;
	if(cy-1>=0&&vis[cx][cy-1])
		temp++;
	vis[cx][cy]=true;
	dfs(no-1,nx,ny,sum+temp);
	vis[cx][cy]=false;
	dfs(no,nx,ny,sum);
}
int main(){    
    freopen("t.txt","r",stdin);
	freopen("B_out.txt","w",stdout);
	int T,Case=1;
	scanf("%d",&T);
	
	while(T--){
		scanf("%d%d%d",&R,&C,&n);
		printf("Case #%d: ",Case++);
		if(R>C)
			Swap(R,C);
		//if(n<=C){
		//	printf("0\n");
		//	continue;
		//}
		ans=R*C*R*C;
		memset(vis,0,sizeof(vis));
		dfs(n,0,0,0);
		printf("%d\n",ans);
		
	}
    return 0;
}