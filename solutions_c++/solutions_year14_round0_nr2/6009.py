#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime> 



double solve(){
	
	double c,f,x;
	scanf("%lf%lf%lf",&c,&f,&x);
	double mn,s,cs=0;
	mn=s=x/2.0;
	for(int i=1;i<=x;i++){
		cs+=c/((i-1)*f+2.0);
		s=x/(i*f+2.0)+cs;
		if(mn>s)mn=s;
	} 
	return mn;
}

int main(){
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		printf("Case #%d: %.7f\n",i,solve());
	}
	
	
	
	
	return 0;
}