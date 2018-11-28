#include<stdio.h>
int main(){
	char c[1000],z;
	int i,x,T,t;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%s",c);
		z = 0;
		x = 0;
		for(i=0;c[i]!=0;i++){
			if(c[i]!=z){
				z = c[i];
				x++;
			}
		}
		if(z=='+')
			x--;
		printf("Case #%d: %d\n",t,x);
	}
}
