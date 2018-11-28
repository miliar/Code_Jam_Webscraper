#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

#define N 1000005

map<int, int> used;

int main() {
	int ncas, n;	
	scanf("%d", &ncas);
	for (int cas = 1; cas <= ncas; cas++) {
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		} else {
			used.clear();
			int ori = n;
			int count = 0;
			while (used.size() < 10) {
				n = ori * (count + 1);
				while (n) {
					int x = n % 10;
					used[x] = 1;
					n /= 10;
				}
				count += 1;
			}
			printf("%d\n", ori * count);
		}
	}
	return 0;
}