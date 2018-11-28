#include <stdio.h>
#include <string>
#include <set>
#include <math.h>

#ifndef MAX
#define MAX 200
#endif
#ifndef YES
#define YES (char*)"YES"
#endif
#ifndef NO
#define NO (char*)"NO"
#endif

using namespace std;

FILE *in, *out;
int mat[MAX][MAX];
int T, N, M, t;
char* res;

bool is_valid_lin(int lin, int col) {
	for (int j = 0; j < M; ++j)
		if (mat[lin][col] < mat[lin][j])
			return false;
	return true;
}

bool is_valid_col(int lin, int col) {
	for (int i = 0; i < N; ++i)
		if (mat[lin][col] < mat[i][col])
			return false;
	return true;
}

char* is_possible() {
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			if (!is_valid_lin(i, j) && !is_valid_col(i, j))
				return NO;
	return YES;
}

int main() {
	in = fopen("B-large.in", "r");
	out = fopen("B.out", "w");
	
	fscanf(in, "%d ", &T);
	
	for(int t = 1; t <= T; ++t)
	{
		fscanf(in, "%d %d ", &N, &M);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				fscanf(in, "%d ", &mat[i][j]);
		res = is_possible();
		fprintf(out, "Case #%d: %s\n", t, res);
	}
	
	return 0;
}
