#include<cmath>
#include<cstdio>
#include<algorithm>

using namespace std;

int main(void){
	int T;
	int cnt[1010];
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		int D, tot, ans;
		scanf("%d", &D);
		for(int j = 0; j < D; j++)
			scanf("%d", &cnt[j]);
		sort(cnt, cnt+D);
		ans = cnt[D-1];
		for(int j = 1; j <= 1000; j++){
			int tmpans = j;
			for(int k = 0; k < D; k++){
				if(cnt[k] <= j) continue;
				if(cnt[k]%j) tmpans += (cnt[k]/j);
				else tmpans += (cnt[k]/j-1);
			}
			if(tmpans < ans) ans = tmpans;
		}
		printf("%d\n", ans);
	}
	return 0;
}