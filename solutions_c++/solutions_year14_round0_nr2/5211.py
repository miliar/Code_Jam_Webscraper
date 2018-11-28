#include<bits/stdc++.h>
int main()
{
	int t,i=1;
	double c,f,x,ans,d,y,z;
	scanf("%d",&t);
	while(t--){
		scanf("%lf%lf%lf",&c,&f,&x);
		ans=0.0;
		z=2.0;
		y=(c/z)+(x/(z+f));
		while(y<(x/z)){
			ans=ans+(c/z);
		//	printf("%lf\n",c/z);
			z=z+f;
			y=(c/z)+(x/(z+f));
		}
		//printf("%lf\n",(x/z));
		ans=ans+(x/z);
		printf("Case #%d: %.7lf\n",i++,ans);
	}
	return 0;
}
