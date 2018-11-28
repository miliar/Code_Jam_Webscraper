#include<cstdio>
#include<iostream>
using namespace std;
double C,F,X;
double calc(int num){
}
void solve(int T){
	scanf("%lf%lf%lf",&C,&F,&X);
	printf("Case #%d: ",T);
	double delta=2,ti=0,ans=1e10;
	for(int i=1;i<=10000000;++i){
		ans=min(ans,ti+X/delta);
		ti+=C/delta;
		delta+=F;
	}
	printf("%.6lf\n",ans);
}
int main(){
	freopen("Blarge.in","r",stdin);
	freopen("Blarge.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int i=1;i<=test;++i)solve(i);
	return 0;
} 
