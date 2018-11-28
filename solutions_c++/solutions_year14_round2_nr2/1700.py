#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<queue>
#include<list>
#include<vector>
#define LL long long
#define INF 0x7fffffff
#define For(i,a,b) for(int i=a; i<b; ++i)
using namespace std;
typedef pair<int,int> ii;
int main(){
	int T;
	cin>>T;
	for(int cas=1; cas<=T; ++cas){
		LL A, B, K;
		cin>>A>>B>>K;
		int cnt=0;
		for(int i=0; i<A; ++i){
			for(int j=0; j<B; ++j){
				if((i&j) <K) cnt++;
			}
		}
		printf("Case #%d: %d\n", cas, cnt);
	}
		
	return 0;
}
