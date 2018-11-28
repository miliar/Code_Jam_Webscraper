#include <bits/stdc++.h>
using namespace std;

typedef int64_t Num;
#define PRINUM PRId64
#define SCANUM SCNd64

void handle_case(int case_num) {
	int n_tiles, complexity, n_students;
	scanf(" %d %d %d", &n_tiles, &complexity, &n_students);
	int next_tile = 0;

	vector<Num> tiles;
	while (next_tile < n_tiles) {
		Num i_tile = 0;
		for (int i = 0; i < complexity; i++) {
			i_tile *= n_tiles;
			i_tile += next_tile++ % n_tiles;
		}
		tiles.push_back(i_tile);
	}

	if (tiles.size() <= n_students) {
		for (int i = 0; i < tiles.size(); i++) {
			printf("%" PRINUM, tiles[i] + 1);
			if (i != tiles.size() - 1)
				printf(" ");
		}
	} else {
		printf("IMPOSSIBLE");
	}
}

int main(void) {
	int n_cases;
	scanf(" %d", &n_cases);
	for (int case_num = 1; case_num <= n_cases; case_num++) {
		printf("Case #%d: ", case_num);
		handle_case(case_num);
		printf("\n");
	}

	return 0;
}
