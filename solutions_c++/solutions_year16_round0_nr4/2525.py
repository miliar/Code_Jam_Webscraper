// Problem D. Fractiles
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d:", ti);
		for (int i = 1; i <= S; i++) printf(" %d", i);
		printf("\n");
	}

	return 0;
}
