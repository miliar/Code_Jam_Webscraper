#include<stdio.h>
#include<algorithm>
using namespace std;
int c[100][100];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)
				scanf("%d",&c[i][j]);
		for(int i=1;i<=100;i++){
			for(int j=0;j<a;j++){
				int d=100;
				int e=0;
				for(int k=0;k<b;k++){
					if(c[j][k]){
						d=min(d,c[j][k]);
						e=max(e,c[j][k]);
					}
				}
				if(d==e&&e==i)for(int k=0;k<b;k++)c[j][k]=0;
			}
			for(int j=0;j<b;j++){
				int d=100;
				int e=0;
				for(int k=0;k<a;k++){
					if(c[k][j]){
						d=min(d,c[k][j]);
						e=max(e,c[k][j]);
					}
				}
				if(d==e&&e==i)for(int k=0;k<a;k++)c[k][j]=0;
			}
		}
		bool ok=true;
		for(int i=0;i<a;i++)
			for(int j=0;j<b;j++)if(c[i][j])ok=false;
		printf("Case #%d: %s\n",t+1,ok?"YES":"NO");
	}
}