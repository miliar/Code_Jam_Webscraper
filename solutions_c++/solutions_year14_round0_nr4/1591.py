#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

const int MAXN = 1003;

double fst[MAXN], scd[MAXN];
bool vst[MAXN];

int solve1(int N){
	int ret = N, hd1, ed1, hd2, ed2;
	hd1 = hd2 = 0;
	ed1 = ed2 = N - 1;
	for (int t = 0; t < N; ++t){
		if (fst[hd1] < scd[hd2]){
			--ret;
			++hd1;
			--ed2;
		}
		else{
			++hd1;
			++hd2;
		}
	}

	return ret;
}

int solve2(int N){
	int ret = N, i, j, pre = 0;
	bool flag;
	for (i = 0; i < N; ++i){
		for (flag=false, j = pre; j < N && (!flag); ++j){
			if (scd[j] > fst[i]){
				vst[j] = true;
				flag = true;
				pre = j + 1;
				--ret;
			}
		}
	}

	return ret;
}

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int T, N, ret1, ret2, idx;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases){
		scanf("%d", &N);
		memset(fst, 0, sizeof(fst));
		memset(scd, 0, sizeof(scd));
		
		for (int i = 0; i < N; ++i) scanf("%lf", &fst[i]);
		for (int i = 0; i < N; ++i) scanf("%lf", &scd[i]);

		std::sort(fst, fst+N);
		std::sort(scd, scd+N);
		
		ret1 = solve1(N);
		ret2 = solve2(N);

		printf("Case #%d: %d %d\n", cases, ret1, ret2);
	}

	return 0;
}