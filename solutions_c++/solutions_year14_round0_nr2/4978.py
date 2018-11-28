#include <stdio.h>
#include<conio.h>
int main(){
		freopen("B-large.in","r",stdin);
	freopen("code.out","w",stdout);
		int t=0,i=0,j=0;
	double d=0.0000000,c=0.0000000,f=0.0000000,x=0.0000000,b=0.0000000,p=0.0000000,g[100];

	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%lf %lf %lf",&c,&f,&x);
	b=2.0000000;
	p=0.0000000;	
		while(c/b+x/(b+f)<x/b){
			p+=c/b;			
			b+=f;
		}
	
p+=x/b;

g[i]=p;	
}
	
	
		for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
	printf("%0.07lf\n",g[i]);}
	
	
	
	
	
	
	
return 0;}
