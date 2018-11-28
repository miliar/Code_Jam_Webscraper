#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
using namespace std;
bool was[10];
void digits(long long a, int &k){
	while(a){
		int b=a%10;
		if(!was[b]){
			was[b]=true;
			++k;
		}
		a/=10;
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int ci=1;ci<=t;++ci){		
		int n,k=0;
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",ci);
		}else{
			for(int i=0;i<10;++i){
				was[i]=false;
			}
			long long a=n;
			while(k<10){
				digits(a,k);
				a+=n;
			}
			a-=n;
			printf("Case #%d: %d\n",ci,a);
		}
	}
	return 0;
}
