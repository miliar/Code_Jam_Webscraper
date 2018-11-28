#include <bits/stdc++.h>
using namespace std;
char S[110];
int main(){
	int t, n;
	scanf("%d", &t);
	for(int c=1; c<=t; c++){
		scanf("%s", S);
		n = strlen(S);
		printf("Case #%d: ", c);
		S[n] = '+';
		int total = 0;
		for(int i=n-1; i>=0; i--){
			if(S[i]!=S[i+1]) total++;
		}
		printf("%d\n", total);
	}
	return 0;
}