#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#define N_MAX 10010
using namespace std;

int fi[N_MAX];
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("large.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cnt = 1; cnt <= T; cnt++){
		printf("Case #%d: ", cnt);
		int N, C;
		scanf("%d%d", &N, &C);
		for(int i = 0; i < N; i++) scanf("%d", &fi[i]);
		sort(fi, fi + N);
		int ans = 0;
		for(int i = 0; i < N; i++){
			ans ++;
			int ub = N, lb = i;
			while(ub - lb > 1){
				int mid = (ub + lb) / 2;
				if(fi[mid] <= C - fi[i]) lb = mid;
				else ub = mid;
			}
			if(lb == i) continue;
			for(int j = lb + 1; j < N; j++) fi[j - 1] = fi[j];
			N --;
		}
		printf("%d\n", ans);
	}
	return 0;
}
