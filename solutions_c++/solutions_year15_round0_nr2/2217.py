#include <cstdio>
#include <cstdlib>
#include <cstring>



using namespace std;

int get_times(int total, int portion) {
	if (portion == 0) return 1001;
	if (total == 0) return 0;
	else return (total - 1) / portion;
}

int main(int argc, char const *argv[])
{
	int T, D, P[1001];
	int times, max, maxTotal;
	scanf("%d", &T);
	for(int r = 0; r < T; ++r){
		scanf("%d", &D);
		max = 0;
		// printf("fuck!\n");
		for(int i = 1; i <= D; ++i){
			scanf("%d", &P[i]);
			max = (max > P[i]) ? max : P[i];
		}
		// printf("fuck2! MAX is %d\n", max);
		maxTotal = 1001;
		// times = 0;

		for(int i = max; i >= 1; --i) {
			times = 0;
			for(int j = 1; j <= D; ++j){
				times += get_times(P[j], i);

			}
			// printf("Times is %d, %d, %d\n", times, i, times + i);
			maxTotal = (maxTotal > times + i) ? (times + i) : maxTotal;
		}
		// printf("fuck3!\n");
		printf("Case #%d: %d\n", r + 1, maxTotal);
	}
	



	return 0;
}

// W