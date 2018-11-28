#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;

int main(){
	int times;
	scanf("%d", &times);
	for (int t=1; t<=times; t++){
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		if (k == s){
			unsigned long long location = 1;
			printf("Case #%d:", t);
			for (unsigned long long i=1; i<c; i++){
				location = location * k + 1;
			}
			for (unsigned long long i=0; i<s; i++){
				printf(" %llu", location * i + 1);
			}
			printf("\n");
		}else{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}
