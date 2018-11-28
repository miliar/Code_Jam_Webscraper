#include <cstdio>
#include <cstring>

double wx[1005];
double wy[1005];
int N;

int v[1005];
int mx[1005], my[1005];

int War(int x) {
	for (int y = 0; y  < N; y++)
		if (wx[x] > wy[y] && !v[y]) {
			v[y] = 1;
			if (my[y] == -1 || War(my[y])) {
				my[y] = x; mx[x] = y;
				return 1;
				}
			}

	return 0;
	}

int D_War(int y) {
	for (int x = 0; x  < N; x++)
		if (wx[x] < wy[y] && !v[x]) {
			v[x] = 1;
			if (mx[x] == -1 || D_War(mx[x])) {
				my[y] = x; mx[x] = y;
				return 1;
				}
			}

	return 0;
	}

int main(void) {
	int T;
	int count;

	scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		scanf("%d", &N);
		
		for (int j = 0; j < N; j++)
			scanf("%lf", &wx[j]);

		for (int j = 0; j < N; j++)
			scanf("%lf", &wy[j]);

		printf("Case #%d: ", i);

		count = 0;
		memset(my, -1, sizeof(my));
		for (int x = 0; x < N; x++) {
			memset(v, 0,sizeof(v));
			
			if (War(x)) 
				count ++;
			}

		printf("%d ", count);

		count = 0;
		memset(mx, -1, sizeof(mx));
		for (int y = 0; y < N; y++) {
			memset(v, 0,sizeof(v));
			
			if (D_War(y)) 
				count ++;
			}

		printf("%d\n",N - count);

		}
	return 0;
	}
