#include <stdio.h>

int main (){
freopen("a.txt","w",stdout);
double x,c,f,total,temp,r;
int t,k=1;
scanf("%d",&t);
while(t--){r=2.0;
	scanf("%lf %lf %lf",&c,&f,&x);
	total=x/r;
	temp=0.0;
//	printf("lopout");
	while(1){
	//	printf("lopin");
		temp+=c/r;
		r=r+f;
		if(total>temp+x/r)
		total=temp+x/r;
		else
		break;
	}
	printf("Case #%d: %.7lf\n",k,total);
    k++;
}
return 0;
}
