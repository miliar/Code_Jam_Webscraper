#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<string>
#include<cstring>
using namespace std;
long long int A, B, K;

int main(){
	int testcase;
	scanf("%d", &testcase);
	int cnt=0;
	while(testcase--){
		scanf("%lld%lld%lld", &A, &B, &K);
		int ans=0;
		for(int i=0; i<A; ++i){
			for(int j=0;j<B;++j){
				int tmp = i&j;
				if(tmp<K)ans++;
			}
		}
		printf("Case #%d: %d\n", ++cnt,ans);
	}
	return 0;
}
