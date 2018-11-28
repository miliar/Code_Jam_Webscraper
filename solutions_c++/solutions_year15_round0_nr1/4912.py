#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main(){
	int T; scanf("%d", &T);
	for(int t=1;t<=T;t++){
		int N; scanf("%d ", &N);
		int ans = 0;
		int sum = 0;
		for(int i=0;i<N+1;i++){
			char c; scanf("%c", &c);
			//if(c == ' ') { i--; continue;}
			int k = c-'0';
			if(sum < i){
				ans += i-sum;
				sum = i;
			}
			sum += k;
		}
		printf("Case #%d: %d\n", t, ans);
	}
}