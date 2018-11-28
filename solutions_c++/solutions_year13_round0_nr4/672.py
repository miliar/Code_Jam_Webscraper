#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int after[2097152];
int N;
int key[25][201];
int type[25];
int key_num[201];

static const int bp[32] =
{
  0, 1, 28, 2, 29, 14, 24, 3, 30, 22, 20, 15, 25, 17, 4, 8,
  31, 27, 13, 23, 21, 19, 16, 7, 26, 12, 18, 6, 11, 5, 10, 9
};

int solve(int cur) {
	int t = cur;
	int i, j;
	int ans = 0;
	if(cur == (1 << N) - 1) {
		return 1;
	}
	if(after[cur] > 0) {
		return 1;
	}
	if(after[cur] == -1) {
		return 0;
	}
	t = cur;
	for(i = 1; i <= N; i++, t>>=1) {
		if(!(t&1)) {
			if(key_num[type[i]]) {
				key_num[type[i]]--;
				for(j = 1; j <= key[i][0]; j++) {
					key_num[key[i][j]]++;
				}
				
				ans = solve(cur | (1 << (i-1)));
				
				key_num[type[i]]++;
				for(j = 1; j <= key[i][0]; j++) {
					key_num[key[i][j]]--;
				}
				
				if(ans) {
					after[cur] = cur | (1 << (i-1));
					return ans;
				}
			}
		}
	}
	after[cur] = -1;
	return ans;
}

void print(FILE *fp) {
	int cur = 0;
	int final = (1 << N) - 1;
	int c;
	while(cur != final) {
		c = cur ^ after[cur];
		fprintf(fp, " %d", 1 + bp[((unsigned int)((c & -c) * 0x077CB531U)) >> 27]);
		cur = after[cur]; 
	}
	fprintf(fp, "\n");
}

int main(void) {
	int T;
	int i, j, k;
	int ans;
	int tk;
	int K;
	FILE *fin, *fout;
	fin = fopen("D.in", "r");
	fout = fopen("D.out", "w+");
	fscanf(fin, "%d", &T);
	for(i = 1; i <= T; i++) {
		fprintf(stdout, "%d\n", i);
		fflush(stdout);
		memset(after, 0, sizeof(after));
		memset(key, 0, sizeof(key));
		memset(type, 0, sizeof(type));
		memset(key_num, 0, sizeof(key_num));
		
		fscanf(fin, "%d%d", &K, &N);
		for(j = 1; j <=K;j++) {
			fscanf(fin, "%d", &tk);
			key_num[tk]++;
		}
		
		for(j = 1; j <=N; j++) {
			fscanf(fin, "%d%d", &type[j], &key[j][0]);
			for(k = 1; k <=key[j][0];k++) {
				fscanf(fin, "%d", &key[j][k]);
			}
		}
		ans = solve(0);
		
		fprintf(fout, "Case #%d:", i);
		if(ans) {
			print(fout);
		}
		else {
			fprintf(fout, " IMPOSSIBLE\n");
		}
	}
	return 0;
}
