#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);

	for(int c = 1; c <= T; c++) {
		int Smax;
		char shyness[1010];
		scanf("%d", &Smax);
		int result = 0;
		int stoodup = 0;
		scanf("%s", shyness);
		for(int i = 0; shyness[i]; i++) {
			int n = shyness[i] - '0';
			while(i > stoodup) {
				result++;
				stoodup++;
			}

			stoodup += n;
		}

		printf("Case #%d: %d\n", c, result);
	}

	return 0;
}
