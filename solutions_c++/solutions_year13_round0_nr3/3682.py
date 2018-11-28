#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;


typedef long long int LL;

int T,A,B;
int v[14];
LL p[50];

bool pal(LL a){
	int ct = 0;
	while(a!=0){
		v[ct]=a%10;
		a/=10;
		ct+=1;
	}
	for(int i=0;i<ct;i++){
		if(v[i] != v[ct-1-i]) return false;
	}
	return true;
}

int main(){

	int ct=0;
	for(LL i=0;i<=10000000;i++){
		if(pal(i)){
			LL a=i*i;
			if(pal(a)){p[ct]=a;ct+=1;}
		}
	}

	scanf("%d ", &T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d %d ",&A,&B);
		int sol=0;
		for(int i=0;i<ct;i++){ 
			if(p[i] >= A && p[i] <= B) sol+=1;
		}
		printf("Case #%d: %d\n",cas,sol);
	}
	
	return 0;
}
