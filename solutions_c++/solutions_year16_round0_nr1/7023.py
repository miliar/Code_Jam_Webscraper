#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int T,N,I;
	scanf("%d",&T);
	for(I=0;I<T;I++){
		scanf("%d",&N);
		printf("Case #%d: ",I+1);
		int i,j;
		if(N==0){
			printf("INSOMNIA\n");
		}
		else{
			int d[10]={},now=0;
			while(1){
				now+=N;
				int tnow=now,t=1;
				while(tnow!=0){
					d[tnow%10]=1;
					tnow/=10;
				}
				for(i=0;i<10;i++){
					if(d[i]==0){
						t=0;
						break;
					}
				}
				if(t==1){
					printf("%d\n",now);
					break;
				}
			}
		}
	}
	return 0;
}