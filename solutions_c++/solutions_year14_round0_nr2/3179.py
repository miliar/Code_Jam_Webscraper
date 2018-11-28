#include<cstdio>
int main(){
	freopen("B-large.in","rt",stdin);
	freopen("o2.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int _=1;_<=t;_++){
		printf("Case #%d: ",_);
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		int n=(int)(X/C-2/F);
		if(n<0) n=0;
		double sum=X/(2+n*F);
		for(int i=0;i<n;i++){
			sum+=C/(2+(i*F));
			//printf("%lf\n",C/(2+(i*F)));
		}
		printf("%.7lf\n",sum);
	}
	return 0;
}