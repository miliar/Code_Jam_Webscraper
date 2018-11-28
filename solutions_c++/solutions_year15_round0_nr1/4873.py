#include<stdio.h>

int main(){
	int t,Smax,i,p=0;
	long int standing,minInvites;
	char str[1005];
	scanf("%d",&t);
	while(p<t){
		standing=minInvites=0;
		scanf("%d %s",&Smax,str);
		
		for(i=0;i<=Smax;i++){
			if(standing<i){
				minInvites+=(i-standing);
				standing+=(int)str[i]-48+(i-standing);
			}
			else{
				standing+=(int)str[i]-48;
			}
		}
		
		printf("Case #%d: %d\n",++p,minInvites);
	}
}
