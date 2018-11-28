#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 52

// Lists
int N;
typedef struct{
	int seq[MAXN];
}LIST;
LIST mat[MAXN*2];

// Comparison function
bool cmp(LIST a, LIST b){
	for(int i = 0; i < N; i++)
		if(a.seq[i] != b.seq[i]) return a.seq[i] < b.seq[i];
	return false;
}

// Mark used
bool rowOK[MAXN], colOK[MAXN];
bool rowUsed[MAXN][2502], colUsed[MAXN][2502];

// Final matrix
int ans[MAXN][MAXN];

// Backtracking
bool done;
void backtrack(int nowID){

	int tmp[MAXN];

	// End
	if(nowID == 2*N-1){

		// Output
		for(int i = 0; i < N; i++){
			if(!rowOK[i]){
				for(int j = 0; j < N; j++)
					printf(" %d", ans[i][j]);
				done = true;
				break;
			}
			if(!colOK[i]){
				for(int j = 0; j < N; j++)
					printf(" %d", ans[j][i]);
				done = true;
				break;
			}
		}
		return;
	}

	// Try to put on one column of first row
	for(int i = 0; i < N; i++){
		if(colOK[i]) continue;
		if(ans[0][i] == mat[nowID].seq[0]){

			// Check
			bool ok = true;
			for(int j = 1; j < N; j++)
				if(ans[j][i] != mat[nowID].seq[j] && (ans[j][i] != -1 || rowUsed[j][ mat[nowID].seq[j] ] || colUsed[i][ mat[nowID].seq[j] ]))
					ok = false;
			if(ok){

				// Copy
				for(int j = 0; j < N; j++)
					tmp[j] = ans[j][i];

				// Try
				for(int j = 1; j < N; j++){
					colUsed[i][ mat[nowID].seq[j] ] = true;
					if(tmp[j] == -1){
						rowUsed[j][ mat[nowID].seq[j] ] = true;
						ans[j][i] = mat[nowID].seq[j];
					}
				}
				colOK[i] = true;
				backtrack(nowID+1);
				if(done) return;

				// Recover
				colOK[i] = false;
				for(int j = 1; j < N; j++){
					colUsed[i][ mat[nowID].seq[j] ] = false;
					if(tmp[j] == -1){
						rowUsed[j][ mat[nowID].seq[j] ] = false;
						ans[j][i] = -1;
					}
				}
			}
			break;
		}
	}

	// Try to put on one row of first column
	for(int i = 0; i < N; i++){
		if(rowOK[i]) continue;
		if(ans[i][0] == mat[nowID].seq[0] || ans[i][0] == -1){

			// Check
			bool ok = true;
			for(int j = 1; j < N; j++)
				if(ans[i][j] != mat[nowID].seq[j] && (ans[i][j] != -1 || rowUsed[i][ mat[nowID].seq[j] ] || colUsed[j][ mat[nowID].seq[j] ]))
					ok = false;
			if(ok || ans[i][0] == -1){

				// Copy
				for(int j = 0; j < N; j++)
					tmp[j] = ans[i][j];

				// Try
				for(int j = 0; j < N; j++){
					if(tmp[j] == -1){
						rowUsed[i][ mat[nowID].seq[j] ] = true;
						colUsed[j][ mat[nowID].seq[j] ] = true;
						ans[i][j] = mat[nowID].seq[j];
					}
				}
				rowOK[i] = true;
				backtrack(nowID+1);
				if(done) return;

				// Recover
				rowOK[i] = false;
				for(int j = 0; j < N; j++){
					if(tmp[j] == -1){
						rowUsed[i][ mat[nowID].seq[j] ] = false;
						colUsed[j][ mat[nowID].seq[j] ] = false;
						ans[i][j] = -1;
					}
				}
			}
		}
	}
}

// Main
int main(void)
{
	int tc, cs, i, j;

	// Read Input
	scanf("%d", &tc);
	for(cs = 1; cs <= tc; cs++){
		printf("Case #%d:", cs);
		scanf("%d", &N);

		// Initialize
		memset(rowOK, false, N*sizeof(bool));
		memset(colOK, false, N*sizeof(bool));
		for(i = 0; i < N; i++){
			memset(rowUsed[i], false, 2502*sizeof(bool));
			memset(colUsed[i], false, 2502*sizeof(bool));
			memset(ans[i], -1, N*sizeof(int));
		}

		// Lists
		for(i = 0; i < 2*N-1; i++)
			for(j = 0; j < N; j++)
				scanf("%d", &mat[i].seq[j]);
		
		// Sort
		sort(mat, mat+2*N-1, cmp);

		// Pick first one as first row
		rowOK[0] = true;
		for(i = 0; i < N; i++){
			ans[0][i] = mat[0].seq[i];
			rowUsed[0][ mat[0].seq[i] ] = true;
			colUsed[i][ mat[0].seq[i] ] = true;
		}

		// Backtracking
		done = false;
		backtrack(1);
		printf("\n");
	}
	return 0;
}
