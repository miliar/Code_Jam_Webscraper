#include<stdio.h>
int f[100][100];
int r[100];
int c[100];
int max(int a,int b){return a>b?a:b;}
int min(int a,int b){return a<b?a:b;}
int main(){
	int nd;
	scanf("%d",&nd);
	for(int ni=0;ni<nd;ni++){
		int h,w;
		int i,j;
		scanf("%d %d",&h,&w);
		for(i=0;i<h;i++){
			for(j=0;j<w;j++)scanf("%d",&f[i][j]);
		}
		for(i=0;i<h;i++){
			r[i]=1;
			for(j=0;j<w;j++)r[i]=max(r[i],f[i][j]);
		}
		for(i=0;i<w;i++){
			c[i]=1;
			for(j=0;j<h;j++)c[i]=max(c[i],f[j][i]);
		}
		for(i=0;i<h;i++){
			for(j=0;j<w;j++){
				if(f[i][j]!=min(r[i],c[j]))break;
			}
			if(j!=w)break;
		}
		printf("Case #%d: ",ni+1);
		if(i!=h)printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}