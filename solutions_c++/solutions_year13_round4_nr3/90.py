#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
	int T, N;
	scanf("%d", &T);
	FILE *f = fopen("c-large.out", "w");
	for (int cn = 1; cn <= T; ++cn)
	{
		scanf("%d", &N);
		vector<int> A(N), B(N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &A[i]);
		for (int i = 0; i < N; ++i)
			scanf("%d", &B[i]);

		vector<int> R(N, -1);
		for (int v = 1; v <= N; ++v) {
			for (int i = 0; i < N; ++i)
			{
				if (R[i] != -1) continue;
				bool ispos = true, ispos2 = false;
				// v�� i�� ä����.
				for (int j = i + 1; j < N; ++j)
					if (R[j] == -1 && A[i] >= A[j]) { ispos = false; break; }
				if (!ispos) continue;
				
				if (B[i] == 1) ispos2 = true;
				for (int j = i + 1; j < N && !ispos2; ++j)
					if (R[j] != -1 && B[i] == B[j] + 1) ispos2 = true;

				if (ispos && ispos2) {
					R[i] = v;
					break;
				}
			}
		}

		printf("Case #%d\n", cn);
		fprintf(f, "Case #%d:", cn);
		for (int i = 0; i < N; ++i)
			fprintf(f, " %d", R[i]);
		fprintf(f, "\n");
	}
	fclose(f);
}
