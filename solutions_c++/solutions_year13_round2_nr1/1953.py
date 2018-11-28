#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <limits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int find(int S[], int C, int N, int s, int y) {
	if (y >= N) return N;
	int j = s;
	while (C > S[j] && j < N) {
		C += S[j]; 
		j++;
	}
		
	if (j < N) {
		//find(S, C + C - 1, N, s, y + 1, Y);
		//find(S, C + C - 1, N, s, y + 1, Y);
		return min(find(S, C + C - 1, N, j, y + 1), y + N - j);
		// if (C + C - 1 <= S[j]) {
			// if (y + N - j < Y) Y = y + N - j;
			// if (C > 1) find(S, C + C - 1, N, s, y + 1, Y);
			// break;
		// } else {
			// C += C - 1; y++;
		// }
	} else {
		return y;
	}
	//if (y < Y) Y = y;
	
}
int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		int A, N, S[100];
		scanf("%d %d", &A, &N);
		int Y = 0, C = A;
		
		for (int j = 0; j < N; j++) {
			scanf("%d", &S[j]);
		}
		sort(S, S + N);
		//for (int j = 0; j < N; j++) {
			//printf("%d\n", S[j]);
	//	}
		Y = find(S, C, N, 0, 0);
		printf("Case #%d: %d\n", i, Y);
		
	}
	return 0;
}