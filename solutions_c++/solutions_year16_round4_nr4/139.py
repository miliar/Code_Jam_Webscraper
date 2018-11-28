#include<stdio.h>
#include<algorithm>
using namespace std;
char str[30][30];
int UF[60];
int FIND(int a){
	if(UF[a]<0)return a;
	return UF[a]=FIND(UF[a]);
}
void UNION(int a,int b){
	a=FIND(a);b=FIND(b);if(a==b)return;UF[a]+=UF[b];UF[b]=a;
}
int v[30];
int c[30][30];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;scanf("%d",&a);
		for(int i=0;i<a;i++)scanf("%s",str[i]);
		for(int i=0;i<2*a;i++)UF[i]=-1;
		int ret=999999;
		for(int i=0;i<(1<<(a*a));i++){
			int edge=0;
			for(int j=0;j<a;j++)for(int k=0;k<a;k++){
				c[j][k]=str[j][k]-'0';
				if(i&(1<<(j*a+k)))c[j][k]=1;
				edge+=c[j][k];
			}
			for(int j=0;j<a*2;j++)UF[j]=-1;
			for(int j=0;j<a;j++)for(int k=0;k<a;k++){
				if(c[j][k])UNION(j,a+k);
			}
			for(int j=0;j<a;j++)v[j]=0;
			for(int j=0;j<a;j++)v[FIND(j)]++;
			bool ok=true;
			for(int j=0;j<a;j++){
				if(FIND(j)==j){
					if(-UF[j]!=v[j]*2)ok=false;
				}
				edge-=v[j]*v[j];
			}
			if(edge==0&&ok){
				ret=min(ret,__builtin_popcount(i));
			}
		}
		printf("Case #%d: %d\n",t,ret);
	}
}