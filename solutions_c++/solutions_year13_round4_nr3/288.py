#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>

int A[40];
int B[40];

bool generate(int idx, int n, int* used, int* d, int* lis) {
	if (idx >= n) {
		for(int i=n-1; i >=0; i--) {
			//verify B[i]
			int max = 0;
			for(int j=n-1; j >i; j--)
				if (d[i] > d[j]) {
					if (B[j] > max) max = B[j];
				}
			if (max + 1 != B[i])
				return false;
		}
		for(int i=0 ;i < n; i++)
			printf("%d ", d[i]);
		printf("\n");
		return true;
	}
	for(int v=1; v<=n; v++) {
		if (used[v]) continue;

		// pruning
		//compute LIS
		int max = 0;
		for(int i=0; i<idx; i++) {
			if (v > d[i]) {
				if (lis[i] > max)
					max = lis[i];
			}
		}
		max++;
		if (A[idx] != max) continue;
		lis[idx] = max;

		bool bad = false;
		for(int i=0; i<idx; i++) {
			if (d[i] > v && B[i] <= B[idx]) {
				bad = true;
				break;
			}
		}
		if (bad) continue;

		used[v] = 1;

		d[idx] = v; //assign ith element to v
		if (generate(idx+1, n, used, d, lis))
			return true;
		used[v] = 0;
	}
	return false;
}

void solve(int n) {
	int used[100];
	memset(used,0,sizeof(used));
	int d[100];
	int lis[100];
	generate(0, n, used, d, lis);
}

int main() {
	int problem;
	setbuf(stdout, NULL);
	
	scanf("%d\n", &problem);
	
	for(int pi=0; pi<problem; pi++) {
		int N;
		scanf("%d", &N);
		for(int i=0; i<N; i++)
			scanf("%d", &A[i]);
		for(int i=0; i<N; i++)
			scanf("%d", &B[i]);
		
		printf("Case #%d: ", pi+1);
		solve(N);

	}
	return 0;
}
