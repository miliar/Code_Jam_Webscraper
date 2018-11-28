#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
int n,j;
int  str[40];
void get(int x){
	str[0]=1;
	int wei=0;
	while(x){
		wei++;
		str[wei]=(x&1);
		x=x>>1;
	}
	while(wei<(n/2-2)) wei++,str[wei]=0;
	str[wei+1]=1;
	for (int i=0;i<(n/2);i++){
		printf("%d",str[i]);
	}
	for (int i=0;i<(n/2);i++){
		printf("%d",str[i]);
	}
}
void work(int k){
	long long ret=0;
	for (int i=0;i<(n/2);i++){
		ret=ret*k+str[i];
	}
	printf(" %lld",ret);
}
int main(){
	int T,ca=1;
	scanf("%d",&T);
	scanf("%d%d",&n,&j);
	printf("Case #1:\n");
	for (int i=0;i<j;i++){
		get(i);
		for (int k=2;k<11;k++){
			work(k);
		}
		printf("\n");
	}
	return 0;
}
