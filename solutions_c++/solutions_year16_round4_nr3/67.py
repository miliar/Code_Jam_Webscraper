#include<bits/stdc++.h>
using namespace std;
int f[500];
bool s[500];
int find(int x){
	if(f[x]==x) return x;
	return f[x]=find(f[x]);
}
void uni(int x,int y){
	int fx=find(x),fy=find(y);
	if(fx!=fy) f[fx]=fy;
}
int main(){
	int T,a[500];
	scanf("%d",&T);
	for(int cs=1;cs<=T;cs++){
		int r,c;
		bool ans=false;
		scanf("%d%d",&r,&c);
		for(int i=0;i<(r+c)*2;i++){
			scanf("%d",&a[i]);
			a[i]--;
		}
		for(int i=0;i<(1<<r*c);i++){
			bool gg=false;
			for(int j=0;j<(r*c+r+c)*2;j++){
				f[j]=j;
			}
			for(int j=0;j<r*c;j++){
				if(i&(1<<j)){
					s[j]=1;
				}
				else{
					s[j]=0;
				}
			}
			for(int j=0;j<r;j++){
				for(int k=0;k+1<c;k++){
					uni((j*c+k)<<1|1,(j*c+k+1)<<1);
				}
			}
			for(int j=0;j+1<r;j++){
				for(int k=0;k<c;k++){
					uni((j*c+k)<<1|s[j*c+k],((j+1)*c+k)<<1|s[(j+1)*c+k]^1);
				}
			}
			for(int j=0;j<c;j++){
				uni(r*c*2+j,j<<1|s[j]^1);
			}
			for(int j=0;j<r;j++){
				uni(r*c*2+c+j,(j*c+c-1)<<1|1);
			}
			for(int j=0;j<c;j++){
				uni(r*c*2+c+r+j,(r*c-1-j)<<1|s[r*c-1-j]);
			}
			for(int j=0;j<r;j++){
				uni(r*c*2+c*2+r+j,c*(r-1-j)<<1);
			}
			for(int j=0;j<r+c;j++){
				if(find(r*c*2+a[j<<1])!=find(r*c*2+a[j<<1|1])){
					gg=true;
					break;
				}
			}
			if(!gg){
				ans=true;
				break;
			}
		}
		printf("Case #%d:\n",cs);
		if(!ans) puts("IMPOSSIBLE");
		else{
			for(int i=0;i<r;i++){
				for(int j=0;j<c;j++){
					if(s[i*c+j]) putchar('/');
					else putchar('\\');
				}
				putchar('\n');
			}
		}
	}
	return 0;
}