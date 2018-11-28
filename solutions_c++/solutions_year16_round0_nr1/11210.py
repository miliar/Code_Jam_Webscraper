#include <cstdio>
#include <iostream>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i = 0; i < T; i++){
		unsigned long long N;
		scanf("%llu",&N);
		int arr[10] = {0};
		int stop = 0;
		unsigned long long mult = 1;
		if(!N) printf("Case #%d: INSOMNIA\n",i+1);
		else{
			unsigned long long ans = 0;
			while(stop < 10){
				unsigned long long curr = N*mult;
				ans = curr;
				while(curr){
					if(!arr[curr%10]){
						arr[curr%10] = 1;
						stop++;
					}
					curr /= 10;
				}
				mult++;
			}
			printf("Case #%d: %llu\n",i+1,ans);
		}
	}
}
