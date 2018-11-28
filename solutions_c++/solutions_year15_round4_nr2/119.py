#include<cstdio>
#include<iostream>
using namespace std;
int n,b,a[1010],ans,T;
double v,x,vv[10],xx[10];
int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;++test){
		scanf("%d%lf%lf",&n,&v,&x);
		for(int i=1;i<=n;++i)scanf("%lf%lf",&vv[i],&xx[i]);
		printf("Case #%d: ",test);
		if(n==1){
			if(xx[1]==x)printf("%lf\n",v/vv[1]);
			else printf("IMPOSSIBLE\n");
		}else{
			if(xx[1]!=xx[2]){
				double v1,v2;
				v1=(v*x-xx[2]*v)/(xx[1]-xx[2]);
				v2=v-v1;
				if(v1>=0&&v2>=0)printf("%lf\n",max(v1/vv[1],v2/vv[2]));
				else printf("IMPOSSIBLE\n");
			}else{
				if(xx[1]==x)printf("%lf\n",v/(vv[1]+vv[2]));
				else printf("IMPOSSIBLE\n");
			}
		}
	}
	return 0;
} 
