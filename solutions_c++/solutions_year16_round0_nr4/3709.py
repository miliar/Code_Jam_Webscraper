#include <bits/stdc++.h>
using namespace std;

int t, k, c, s;

int main(){
	scanf("%d\n", &t);
	for(int tc = 0; tc < t; tc++){
		printf("Case #%d:", tc+1);
		scanf("%d%d%d", &k, &c, &s);
		for(int i = 1; i <= s; i++){
			printf(" %d", i);
		}
		printf("\n");
	}
}
