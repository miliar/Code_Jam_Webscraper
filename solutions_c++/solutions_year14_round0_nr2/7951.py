#include<stdio.h>

int main(){

	int t,u=1;
	scanf("%d\n",&t);
while(u<=t){
	long double c,f,x;
	scanf("%llf%llf%llf\n",&c,&f,&x);

long double ans,i=1,ap=0,temp=0;
ans=x/2;
	
	while(ans>=0){
temp=temp+(c/(2+(f*(i-1))));
ap=temp+(x/(2+(f*i)));
	
	if(ap>=ans){
		printf("Case #%d: %0.7llf\n",u,ans);
	break;
	}

		
	

	ans=ap;
	i++;
	
	
}
	u++;
}



	return 0;
}
