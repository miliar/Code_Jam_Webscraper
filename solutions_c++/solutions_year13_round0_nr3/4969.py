#include <iostream>
#include <cstdio>
using namespace std;

long long int ans[100000],ans_n;

bool Check(long long int n){
	bool Same=true;
	long long int Di=1,tmp=n;
	while(tmp){Di*=10; tmp/=10;}
	if(Di!=1)Di/=10;
	while(Di){
		if(n%10==n/Di){n%=Di; n/=10; Di/=100;}
		else {Same=false; break;}
	}
	return Same;
}

void init(){
	ans_n=0;
	for(long long int i=1; i<10000000; i++){
		if(!Check(i))continue;
		long long int tmp=i*i;
		if(Check(tmp)) ans[ans_n++]=tmp;
	}
}

int main(){
	init();
	int T;
	scanf("%d",&T);
	for(int Case=1; Case<=T; Case++){
		int a,b,Ans=0;
		scanf("%d%d",&a,&b);
		for(int i=0; i<ans_n; i++){
			if(ans[i]>=a && ans[i]<=b) Ans++;
			else if(ans[i]>b) break;
		}
		printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}
