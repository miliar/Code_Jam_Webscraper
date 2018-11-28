#include<stdio.h>
#include<algorithm>
using namespace std;
int c[37];
int d[37];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;
		int b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<37;i++)c[i]=d[i]=0;
		for(int i=0;i<b;i++)scanf("%d",c+i);
		double ret=0;
		for(int i=1;i<=a;i++){
			int at=0;
			for(int j=0;j<37;j++)
				if(c[at]+d[at]>c[j]+d[j]||(c[at]+d[at]==c[j]+d[j]&&c[j]>c[at])){
					at=j;
				}
			d[at]++;
			int MiN=9999999;
			for(int j=0;j<37;j++)MiN=min(MiN,c[j]+d[j]);
			int pro=0;
			int u=0;
			for(int j=0;j<37;j++)
				if(MiN==c[j]+d[j]){
					pro+=d[j];
					u++;
				}
			ret=max(ret,36.0*pro/u-i);
		}
		printf("Case #%d: %.8f\n",t,ret);
	}
}