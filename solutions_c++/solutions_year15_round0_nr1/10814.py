#include<stdio.h>

int main(){
	int t,s,K,k[1100],n,y,palmas;
	scanf("%d", &t);
	n=1;
	for(int i=0;i<t;i++){
		palmas=0;
		y=0;
		scanf("%d", &s);
		scanf("%d", &K);
		for(int j=0;j<s+1;j++){
			k[s-j]=K%10;
			K/=10;
		}
		for(int j=0;j<s+1;j++){
			if(palmas<j){
				y+=1;
				palmas+=1;
			}
			palmas+=k[j];
		}	
		printf("Case #%d: %d\n",n,y);
		n+=1;
	}
	return 0;
}
