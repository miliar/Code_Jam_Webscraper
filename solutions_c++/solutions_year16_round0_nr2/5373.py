#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char S[105];
int d(int i, int j){
	if (i == 0){
		return (S[i] == '+' && j == 0 || S[i] == '-' && j == 1) ? 0 : 1;
	}
	if (j == 0){
		if (S[i] == '+'){
			return d(i - 1, 0);
		}
		else{
			return d(i - 1, 1) + 1;
		}
	}
	else{
		if (S[i] == '-'){
			return d(i - 1, 1);
		}
		else{
			return d(i - 1, 0) + 1;
		}
	}
}
int main(){
	int T;
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; ++testcase){
		scanf("%s", S);
		printf("Case #%d: %d\n", testcase, d(strlen(S) - 1, 0));
	}
	return 0;
}