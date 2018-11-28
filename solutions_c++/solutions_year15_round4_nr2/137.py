#include<stdio.h>
#include<algorithm>
using namespace std;
long double EPS=1e-9;
long double d[110];
long double e[110];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a;
		long double b,c;
		scanf("%d%Lf%Lf",&a,&b,&c);
		long double L=9999999;
		long double R=0;
		for(int i=0;i<a;i++){
			scanf("%Lf%Lf",d+i,e+i);
			L=min(L,e[i]);
			R=max(R,e[i]);
		}
		for(int i=0;i<a;i++){
			for(int j=0;j<a-1;j++){
				if(e[j]>e[j+1]){
					swap(d[j],d[j+1]);
					swap(e[j],e[j+1]);
				}
			}
		}
		printf("Case #%d: ",t);
		if(c>R+EPS||c<L-EPS){
			printf("IMPOSSIBLE\n");continue;
		}
		L=0;
		R=1111111111.0;
	//	for(int i=0;i<100;i++){
		//	double M=1;
			long double netsu=0;
			long double taiseki=0;
			for(int j=0;j<a;j++){
				netsu+=d[j]*e[j];
				taiseki+=d[j];
			}
		//	printf("%.12f: %.12f %.12f\n",M,netsu,taiseki*c);
			if(netsu>taiseki*c){
				for(int j=a-1;j>=0;j--){
					long double nn=netsu-d[j]*e[j];
					long double nt=taiseki-d[j];
					if(c+EPS>e[j])break;
					if(nn>nt*c){
						netsu=nn;
						taiseki=nt;
					}else{
						long double x=(netsu-c*taiseki)/(e[j]-c);
						netsu-=x*e[j];
						taiseki-=x;
						break;
					}
				}
			}else{
				for(int j=0;j<a;j++){
					long double nn=netsu-d[j]*e[j];
					long double nt=taiseki-d[j];
					if(c-EPS<e[j])break;
					if(nn<nt*c){
						netsu=nn;
						taiseki=nt;
					}else{
						long double x=(netsu-c*taiseki)/(e[j]-c);
						netsu-=x*e[j];
						taiseki-=x;
						break;
					}
				}
			}
		//	printf("%.12Lf\n",taiseki);
			L=b/taiseki;
//		}
		printf("%.12Lf\n",L);
	}
}