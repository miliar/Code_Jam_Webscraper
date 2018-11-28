#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
using namespace std;
#define ll long long int


ll arr[11];
string str;
ll use;

int check(){
	for(use=0;use<=9;use++){
		if(arr[use]==0) return 0;
	}
	return 1;
}

int main(){
	//string result;
	//stringstream convert;
	ll t,n,i,j,len,k,temp;
	scanf("%lld",&t);
	for(i=1;i<=t;i++){
		scanf("%lld",&n);
		if(n==0){
			printf("Case #%lld: INSOMNIA\n",i);
			continue;
		}
		k=1;
		for(j=0;j<=9;j++) arr[j]=0;
		while(1){
			if(check()==1) break;
			temp = n*k;
			while(temp>0){
				arr[temp%10]++;
				temp/=10;
			}
			k++;
		}
		if(k!=1) n = n*(k-1);
		printf("Case #%lld: %lld\n",i,n);
	}
	return 0;	
}