#include<stdio.h>
int DO(int n){
	char d[10]={};
	int i,c=10,now=0,tmp;
	for(i=1;c;i++){
		now+=n;
		tmp=now;
		while(tmp){
			if(d[tmp%10]==0){
				d[tmp%10]++;
				c--;
			}
			tmp/=10;
		}
	}
	return now;
}
int main(){
	int T,t,n;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",t);
		else
			printf("Case #%d: %d\n",t,DO(n));
	}
}
