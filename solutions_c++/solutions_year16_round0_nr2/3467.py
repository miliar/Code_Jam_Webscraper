#include <bits/stdc++.h>
using namespace std;

int T, TC = 1;
char S[110], d;
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d%c", &T, &d);
	while(T--){
		gets(S);
		int len = strlen(S), ans = 0;
		char cur = S[0];
		for(int i = 1; i < len; i++){
			if(S[i] == cur) continue;
			cur = S[i];
			ans++;
		}
		if(cur == '-') ans++;
		printf("Case #%d: %d\n", TC++, ans);
	}
	return 0;
}
