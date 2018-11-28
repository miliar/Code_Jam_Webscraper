#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
	FILE *stream;
	freopen_s(&stream, "C:\\new\\A-large.in", "r", stdin);
	freopen_s(&stream, "C:\\new\\outlarge.txt", "w", stdout);
	int T;
	scanf_s("%d", &T);

	for (int i = 1; i <= T; i++)
	{
		int b[11];
		memset(b, 0, sizeof(b));
		char N[8];
		int S[21];
		memset(S, 0, sizeof(S));
		scanf_s("%s", N, 8);
		if (N[0] == '0' && N[1] == '\0') printf("Case #%d: INSOMNIA\n", i);
		else {
			int NN = strlen(N);
			int SS = 20 - NN;
			while (!(b[10] && b[1] && b[2] && b[3] && b[4] && b[5] && b[6] && b[7] && b[8] && b[9])) {
				for (int j = 0; j < NN; j++) {
					S[19 - j] += (N[NN - j - 1] - 48);
					if (S[19 - j] > 9) {
						S[19 - j] -= 10;
						S[19 - j - 1]++;
						if (19 - j - 1<SS) SS = 19 - j - 1;
					}
				}
				for (int j = SS; j < 20;j++) b[S[j] + 1] = 1;
			}
			printf("Case #%d: ", i);
			bool t = false;
			for (int j = SS; j < 20;j++) printf("%d", S[j]);
			printf("\n");
		}
	}
	return 0;
}