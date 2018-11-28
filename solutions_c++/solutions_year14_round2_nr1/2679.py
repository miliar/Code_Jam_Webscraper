#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) stdout<<#x<<" = "<<(x)<<endl

const int MAXN = 1024;

int a, n;
int arr[MAXN];

void process(int tt) {
	char str[1000];
	char letters[200];
	int counts[200][200];
	for (int i = 0; i < 200; i++)
		for (int j = 0; j < 200; j++)
			counts[i][j] = 0;



	scanf("%d", &n);
	for (int i = 0; i<n; i++){
		scanf("%s", str);
		if (i == 0) {
			letters[0] = str[0];
			counts[0][i] = 1;
			int letter_idx = 1;
			for (int j = 1; j < strlen(str); j++) {
				if (str[j] != letters[letter_idx - 1]) {
					// counts[letter_idx][i] = 0;
					letters[letter_idx++] = str[j];
				}
				counts[letter_idx - 1][i]++;
			}
			letters[letter_idx] = 0;
		} else {
			// printf(":%s\n", letters);
			if (letters[0] != str[0]) {
				printf("Case #%d: Fegla Won\n", tt);
				return;
			}
			counts[0][i] = 1;
			int letter_idx = 1;
			// printf("%d\n", letter_idx);
			for (int j = 1; j < strlen(str); j++) {
				if (str[j] != letters[letter_idx - 1]) {
					// counts[letter_idx][i] = 0;
					if (letter_idx >= strlen(letters) || str[j] != letters[letter_idx]) {
						printf("Case #%d: Fegla Won\n", tt);
						return;
					}
					// printf("not eq %d %c %d %c\n", j, str[j], letter_idx-1, letters[letter_idx-1]);
					letter_idx++;
				}
				// printf("++%d %d\n", letter_idx - 1, i);
				counts[letter_idx - 1][i]++;
			}
			if (letter_idx < strlen(letters)) {
				printf("Case #%d: Fegla Won\n", tt);
						return;
			}


		}
	}
			// printf(":%s\n", letters);
	int final_score = 0;
	for (int i = 0; i < strlen(letters); i++) {
		sort(counts[i], counts[i] + n);
		// for (int j = 0; j < n; j++) {
		// 	printf("%d ", counts[i][j]);
		// }
		// printf("\n");
		int j = 0;
		while (j < n && counts[i][j] == counts[i][0]) {
			j++;
		}
		if (j == n) {
			continue;
		}
		int start_count = j;
		j = n-1;
		int end_count = 0;
		while (j >= 0 && counts[i][j] == counts[i][n-1]) {
			j--;
			end_count++;
		}
				// printf("emd: %d\?n", end_count);
				// printf("start: %d\n", start_count);
		while (start_count + end_count <= n) {
			if (start_count < end_count) {
				final_score += start_count * (counts[i][start_count] - counts[i][start_count - 1]);
				j = start_count;
				while (j < n && counts[i][j] == counts[i][start_count]) {
					j++;
				}
				start_count = j;
				// printf("start: %d\n", start_count);
			} else {
				final_score += end_count * (counts[i][n - end_count] - counts[i][n - end_count - 1]);
				j = n - end_count - 1;
				int final = counts[i][n - end_count - 1];
				// Eo(j);
			// printf(":%s\n", letters);
// printf("j %d\n", j);
				while (j >= 0 && counts[i][j] == final) {
					j--;
					end_count++;
				}
				// printf("emd: %d, %d %d\n", end_count, start_count + end_count, n);
			}
			// printf("aa%d\n", end_count);

		}

		// printf(":%d\n", start_count);
	}
		printf("Case #%d: %d\n", tt, final_score);
}

int main() {
	// freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt1.in", "r", stdin);
	// freopen("A-large.in", "r", stdin);
	// freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {


		process(tt);

		fflush(stdout);
	}
	return 0;
}
