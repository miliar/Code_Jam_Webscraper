#include<cstdio>

int tab[1010];

int main() {
	int T; scanf("%d", &T);
	for(int _ = 0; _ < T; _++) {
		int N; scanf("%d", &N);
		int max = 0;
		for(int i = 0; i < N; i++) {
			scanf("%d", tab+i);
			if(tab[i] > max) max = tab[i];
		}
		int res = max;
		for(int j = 1; j < max; j++) {
			int time = 0;
			for(int i = 0; i < N; i++) {
				if(tab[i] > j) {
					time += (tab[i]-j)/j+((tab[i]%j)?1:0);
				}
			}
			if(time + j < res) res = time+j;
		}
		printf("Case #%d: %d\n", _+1, res);
	}
	return 0;
}
