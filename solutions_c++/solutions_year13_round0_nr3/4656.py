#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>

int main () {
	std::vector<int> nums = {1,4,9,121,484};

	int T, total;
	int n,m;

	FILE * file = fopen("test.txt", "r"),
			* result = fopen("result.txt", "w");

	fscanf(file, "%d\n", &total);
	T = total + 1;
	while (total) {
		fscanf(file, "%d %d\n", &n, &m);
		int k = 0;
		for (int i = 0; i < 5 ; ++i) {
			if (nums[i] <= m && nums[i] >= n) {
				k++;
			}
		}

		fprintf(result, "Case #%d: %d\n", T-total, k);

		total --;
	}

	fclose(file);
	fclose(result);

	return 0;
}
