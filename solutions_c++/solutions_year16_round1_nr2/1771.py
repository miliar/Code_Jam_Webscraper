
#include <iostream>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for(int n = 1; n <= t; ++n) {
		int size, height_tmp;
		int height[2501] = {0};
		scanf("%d", &size);
		for(int i = 0; i < 2*size*size - size; ++i) {
			scanf("%d", &height_tmp);
			height[height_tmp]++;
		}
		printf("Case #%d: ", n);
		for(int i = 1; i <= 2500; i++) {
			if(height[i] % 2)
				printf("%d ", i);
		}
		printf("\n");
	}

	return 0;
}
