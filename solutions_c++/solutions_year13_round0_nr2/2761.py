/******************************************************************************
 * Directives
 *****************************************************************************/
#ifdef WIN32
#define _CRT_SECURE_NO_WARNINGS
#endif

/******************************************************************************
 * Header Files
 *****************************************************************************/
#include <stdio.h>

/******************************************************************************
 * Constants, Macros, Typedefs, Enums & Structures
 *****************************************************************************/

/******************************************************************************
 * Global & Static Variables
 *****************************************************************************/
int g_N, g_M;
int g_row_min[100];
int g_col_min[100];
int g_data[10000];

/******************************************************************************
 * Global & Static Function Prototypes
 *****************************************************************************/
void runCase();

/******************************************************************************
 * Function Implementations
 *****************************************************************************/
int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <=T; t++) {
		printf("Case #%d:", t);
		runCase();
	}

	return 0;
}

bool chkRow(int r, int c)
{
	int idx = g_M * r;
	int val = g_data[idx + c];
	for (int i = 0; i < g_M; i++) {
		if (g_data[idx] > val) {
			return false;
		}
		idx++;
	}
	return true;
}

bool chkCol(int r, int c)
{
	int idx = c;
	int val = g_data[g_M * r + c];
	for (int i = 0; i < g_N; i++) {
		if (g_data[idx] > val) {
			return false;
		}
		idx += g_M;
	}
	return true;
}

bool chkOk()
{
	// get row min
	int idx = 0;
	for (int r = 0; r < g_N; r++) {
		int min = 100;
		for (int c = 0; c < g_M; c++) {
			if (g_data[idx] < min) {
				min = g_data[idx];
			}
			idx++;
		}
		g_row_min[r] = min;
	}
	// get col min
	for (int c = 0; c < g_M; c++) {
		int min = 100;
		idx = c;
		for (int r = 0; r < g_N; r++) {
			if (g_data[idx] < min) {
				min = g_data[idx];
			}
			idx += g_M;
		}
		g_col_min[c] = min;
	}
	// chk
	idx = 0;
	for (int r = 0; r < g_N; r++) {
		int row_min = g_row_min[r];
		for (int c = 0; c < g_M; c++) {
			int val = g_data[idx];
			idx++;
			if (val == row_min && val == g_col_min[c]) {
				if (chkRow(r, c) == false && chkCol(r, c) == false) {
					return false;
				}
			}
		}
	}
	return true;
}

void runCase()
{
	scanf("%d %d", &g_N, &g_M);

	int len = g_N * g_M;
	for (int i = 0; i < len; i++) {
		scanf("%d", &g_data[i]);
	}

	if (chkOk()) {
		printf(" YES\n");
	} else {
		printf(" NO\n");
	}
}