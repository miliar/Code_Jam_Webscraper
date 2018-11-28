#include<stdio.h>

int main(){
	//freopen("0Q/A-large.in","r",stdin);
	//freopen("0Q/out.txt","w",stdout);


	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){

		int smax;
		scanf("%d",&smax);

		char k;
		int sk,std=0,f=0;
		scanf(" %c",&k);
		sk = k - '0';
		std = sk;
		for(int s=1;s<=smax;s++){
			scanf("%c",&k);
			sk = k - '0';
			if(std<s){
				std++;
				f++;
			}
			std+=sk;
		}
		printf("Case #%d: %d\n",t,f);
	}
	return 0;
}
