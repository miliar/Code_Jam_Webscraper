#include<cstdio>
#include<cmath>
int main(){
	freopen("B_output.txt","w",stdout);
	freopen("B-large.in","r",stdin);

	int t;
	scanf("%d",&t);
	for(int tc=1; tc<=t; tc++){
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		
		int g = floor((x/c - 1) - (2/f));
		printf("Case #%d: ",tc);
		if(g<=-1)
			printf("%.7lf\n",x/2);
		else{
			// print f(g+1)
			double tmp = 0;
			double ans = 0;
			double div = 2;
			for(int i=0; i<=g; i++){
				tmp += 1./div;
				div += f;
			}
			ans += c*tmp;
			ans += x/div;
			printf("%.7lf\n", ans);
		}
	}
}