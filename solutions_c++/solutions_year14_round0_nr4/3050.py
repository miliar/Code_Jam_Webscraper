#include<cstdio>
#include<cstdlib>

const int BRICKS = 1001;

int compare(const void* a, const void* b) {
	if (*(float*)a > *(float*)b) return -1;
	if (*(float*)a < *(float*)b) return 1;
	return 0;
}

void solve(const int case_no) {
	int count;
	scanf("%d", &count);
	float n_bricks[BRICKS] = {0};
	for (int i=0; i < count; i++) {
		scanf("%f", &n_bricks[i]);
	}
	float k_bricks[BRICKS] = {0};
	for (int i=0; i < count; i++) {
		scanf("%f", &k_bricks[i]);
	}
	qsort(n_bricks, count, sizeof(float), compare);	
	qsort(k_bricks, count, sizeof(float), compare);	

	float* n_min = &n_bricks[count-1];
	float* k_min = &k_bricks[count-1];
	float* n_max = &n_bricks[0];
	float* k_max = &k_bricks[0];

	int dwar_p = 0;
	for (int step = count; step > 0; step--) {
		if (*n_min > *k_min) {
			dwar_p++;
			n_min--;
			k_min--;
		} else {
			n_min--;
			k_max++;
		}
	}

	n_min = &n_bricks[count-1];
	k_min = &k_bricks[count-1];
	n_max = &n_bricks[0];
	k_max = &k_bricks[0];

	int war_p = 0;
	for (int step = count; step > 0; step--) {
		if (*n_max > *k_max) {
			war_p++;
			n_max++;
			k_min--;
		} else {
			n_max++;
			k_max++;
		}
	}

	printf("Case #%d: %d %d\n", case_no, dwar_p, war_p);
}

int main(int, char**) {
	int case_no;
	scanf("%d", &case_no);
	for (int i=1; i <= case_no; i++) {
		solve(i);
	}
	return EXIT_SUCCESS;
}
