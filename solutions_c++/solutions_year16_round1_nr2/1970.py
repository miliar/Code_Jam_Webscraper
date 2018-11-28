#include <map>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N;
		scanf("%d", &N);

		map<int, int> M;
		for (int i = 0; i < 2 * N - 1; i++) {
			for (int j = 0; j < N; j++) {
				int h;
				scanf("%d", &h);
				M[h]++;
			}
		}

		bool printed = false;
		printf("Case #%d: ", t);
		map<int, int>::iterator it;
		for (it = M.begin(); it != M.end(); it++) {
			if (it->second & 1) {
				if (printed) printf(" ");
				printed = true;
				printf("%d", it->first);
			}
		}
		printf("\n");
	}

	return 0;
}

