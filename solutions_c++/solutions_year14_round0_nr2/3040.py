#include <stdio.h>

void main(){
	//cookiec clicker
	double r=2.0,c=0,f=0,x=0;//rate r   farmprice c  farmrate f  minpoints x
	int t=0;//test cases


	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	//printf("%.7f",c);
	
	scanf("%d",&t);//scan test case
	//printf("%d",t);

	for(int k=1;k<=t;k++){
	scanf("%lf %lf %lf",&c,&f,&x);
	//printf("c %lf\n f %lf\n x %lf\n\n ",c,f,x);

	double h1=0,h2=-1,st1,st2=0,k1=0,k2=0;;
	
		st1=x/(r+(k1*f));
		if(k1)st2=st2+(c/(r+((k1-1)*f)));
		h1=st1+st2;
		//printf("%.7lf\n",h1);
		k1++;
	while(1){
		
		st1=x/(r+(k1*f));
		if(k1)st2=st2+(c/(r+((k1-1)*f)));
		h2=st1+st2;
		//printf("%.7lf\n",h2);
		k1++;
		if(h2>h1)break;
		h1=h2;
	}
	printf("Case #%d: %.7lf\n",k,h1);

	}
	

}