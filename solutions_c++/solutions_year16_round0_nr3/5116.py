//*
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<algorithm>
#include<vector>
#define all(A) (A).begin(), (A).end()

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int N=32,M=500;

ll convert(int n,int b){
	ll r=0,v=1;
	for(int i=0;i<N/2;i++){
		if(n&(1<<i)){
			r+=v;
		}
		v*=b;
	}
	return r;
}

void print(int n){
	for(int i=N/2-1;i>=0;i--){
		if(n&(1<<i))printf("1");
		else printf("0");
	}
}

int main(){
	freopen("output.txt","w",stdout);
	puts("Case #1:");
	int st=(1<<(N/2-1))+1;
	for(int i=st;i<st+2*M;i+=2){
		print(i);print(i);
		for(int j=2;j<=10;j++){
			printf(" %lld",convert(i,j));
		}
		puts("");
	}
	return 0;
}
//*/