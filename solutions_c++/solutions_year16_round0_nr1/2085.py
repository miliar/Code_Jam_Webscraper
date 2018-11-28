#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int N, n, s;
bool ari[10];

int main(int argc, char** argv) {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &N);
	
	for (int times = 1; times <= N; times++) {
		printf("Case #%d: ", times);
		scanf("%d", &n);
		if (!n) {
			printf("INSOMNIA\n");
			continue;
		}
		
		memset(ari, false, sizeof(ari));
		s = 0;
		for (int i = 1; s < 10; ++i) {
			for (int num = i * n; num > 0 && s < 10; num /= 10) {
				if (!ari[num % 10]) {
					ari[num % 10] = true;
					++s;
				}
			}
			if (s == 10) printf("%d\n", i * n);
		}
	}
	return 0;
}

