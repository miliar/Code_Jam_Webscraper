#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
	int TC,N;
	float arr1[1010];
	float arr2[1010];
	scanf("%d",&TC);
	for (int T=1;T<=TC;T++){
		scanf("%d",&N);
		for (int i=0;i<N;i++){
			scanf("%f",&arr1[i]);
		}
		sort(arr1,arr1+N);
		for (int i=0;i<N;i++){
			scanf("%f",&arr2[i]);
		}
		sort(arr2,arr2+N);
		int cur=0;
		int a=0;
		for (int i=0;i<N;i++){
			if (cur==N) break;
			while(arr2[cur]<arr1[i]){
				cur++;
				if (cur>=N) break;
			}
			if (cur==N) break;
			cur++;
			a++;
		}
		a=N-a;
		int b=0;
		cur=0;
		for (int i=0;i<N;i++){
			if (cur==N) break;
			while(arr1[cur]<arr2[i]){
				cur++;
				if (cur==N) break;
			}
			if (cur==N) break;
			cur++;
			b++;
		}
		printf("Case #%d: %d %d\n",T,b,a);
	}
}