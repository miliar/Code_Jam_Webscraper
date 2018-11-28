#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int T;

int main() {
	freopen("magictrick.in", "r", stdin);
	freopen("magictrick.out", "w", stdout);

	scanf("%d", &T);

	for(int i = 0; i < T; i++) {
		int r1, r2;
		int row1[4], row2[4];
		scanf("%d", &r1);
		for(int r = 0; r < 4; r++) {
			int row[4];
			scanf("%d%d%d%d", &row[0], &row[1], &row[2], &row[3]);

			if(r == r1-1) memcpy(row1, row, sizeof(row));
		}
		scanf("%d", &r2);
		for(int r = 0; r < 4; r++) {
			int row[4];
			scanf("%d%d%d%d", &row[0], &row[1], &row[2], &row[3]);

			if(r == r2-1) memcpy(row2, row, sizeof(row));
		}

		sort(row1, row1+4);
		sort(row2, row2+4);

		int nums[4] = { 0, 0, 0, 0 };
		set_intersection(row1, row1+4, row2, row2+4, nums);

		printf("Case #%d: ", i+1);
		if(!nums[0]) printf("Volunteer cheated!\n");
		else if(!nums[1]) printf("%d\n", nums[0]);
		else printf("Bad magician!\n");
	}
}
