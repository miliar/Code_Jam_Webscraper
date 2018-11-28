#include <cstdio>
#include <map>
#include <list>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int S;
char in[1005];

void solve(){
	scanf("%d%s", &S, in);
	int sum = 0, ans = 0;
	for (int i = 0; i <= S; i++){
		if (sum < i) ans += i - sum, sum = i;
		sum += in[i] - '0';
	}
	printf("%d\n", ans);
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}
