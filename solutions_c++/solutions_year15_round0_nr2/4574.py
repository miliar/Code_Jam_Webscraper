#include <cstdio>
#include <algorithm>

using namespace std;

int cnt[10];
int ans;
void dfs( int sp){
	int idx;

	for (int i = 9; i > 0; i--){
		if (cnt[i] > 0){
			idx = i;
			break;
		}
	}
	if (idx > 3){
		int tmp = cnt[idx];
		cnt[idx] = 0;
		ans = min(ans, sp + idx);
		for (int i = 1; i <= idx/2; i++){
			cnt[i] += tmp;
			cnt[idx - i] += tmp;
			dfs(sp + tmp);
			cnt[i] -= tmp;
			cnt[idx - i] -= tmp;
		}
		cnt[idx] = tmp;
	}
	else{
		ans = min(ans, sp + idx);
	}
}

int main(){
	int tc;
	int tmp;
	int testcase = 1;
	scanf("%d", &tc);
	while (tc--){
		for (int i = 0; i <= 10; i++){
			cnt[i] = 0;
		}
		
		int d;
		scanf("%d", &d);
		for (int i = 0; i < d; i++){
			scanf("%d", &tmp);
			cnt[tmp]++;
		}
		ans = 10000;
		dfs(0);
		printf("Case #%d: ", testcase);
		testcase++;
		printf("%d\n", ans);
	}
	return 0;
}