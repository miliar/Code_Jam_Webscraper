
#include <iostream>
#include <string>

#define ALPHA_SIZE 15
#define NUM_SIZE 10
#define E 0
#define F 1
#define G 2
#define H 3
#define I 4
#define N 5
#define O 6
#define R 7
#define S 8
#define T 9
#define U 10
#define V 11
#define W 12
#define X 13
#define Z 14

using namespace std;

bool alpha_cnt_chk(int *ar);

int main() {
	int t = 0;
	scanf("%d", &t);

	for(int i = 1; i <= t; i++) {
		int alpha_cnt[ALPHA_SIZE] = {0}, cnt[NUM_SIZE] = {0};
		char source[2001];
		scanf("%s", source);

		for(int j = 0; j < strlen(source); ++j) {
			switch(source[j]) {
			case 'E' : alpha_cnt[E]++; break;
			case 'F' : alpha_cnt[F]++; break;
			case 'G' : alpha_cnt[G]++; break;
			case 'H' : alpha_cnt[H]++; break;
			case 'I' : alpha_cnt[I]++; break;
			case 'N' : alpha_cnt[N]++; break;
			case 'O' : alpha_cnt[O]++; break;
			case 'R' : alpha_cnt[R]++; break;
			case 'S' : alpha_cnt[S]++; break;
			case 'T' : alpha_cnt[T]++; break;
			case 'U' : alpha_cnt[U]++; break;
			case 'V' : alpha_cnt[V]++; break;
			case 'W' : alpha_cnt[W]++; break;
			case 'X' : alpha_cnt[X]++; break;
			case 'Z' : alpha_cnt[Z]++; break;
			}
		}
		while(alpha_cnt[Z]) {	// 0
			alpha_cnt[Z]--; alpha_cnt[E]--; alpha_cnt[R]--; alpha_cnt[O]--;
			cnt[0]++;
		}
		while(alpha_cnt[W]) {	// 2
			alpha_cnt[T]--; alpha_cnt[W]--; alpha_cnt[O]--;
			cnt[2]++;
		}
		while(alpha_cnt[U]) {	// 4
			alpha_cnt[F]--; alpha_cnt[O]--; alpha_cnt[U]--; alpha_cnt[R]--;
			cnt[4]++;
		}
		while(alpha_cnt[X]) {	// 6
			alpha_cnt[S]--; alpha_cnt[I]--; alpha_cnt[X]--;
			cnt[6]++;
		}
		while(alpha_cnt[G]) {	// 8
			alpha_cnt[E]--; alpha_cnt[I]--; alpha_cnt[G]--; alpha_cnt[H]--; alpha_cnt[T]--;
			cnt[8]++;
		}

		while(alpha_cnt[O]) {	// 1
			alpha_cnt[O]--; alpha_cnt[N]--; alpha_cnt[E]--;
			cnt[1]++;
		}
		while(alpha_cnt[T]) {	// 3
			alpha_cnt[T]--; alpha_cnt[H]--; alpha_cnt[R]--; alpha_cnt[E]-= 2;
			cnt[3]++;
		}
		while(alpha_cnt[F]) {	// 5
			alpha_cnt[F]--; alpha_cnt[I]--; alpha_cnt[V]--; alpha_cnt[E]--;
			cnt[5]++;
		}
		while(alpha_cnt[V]) {	// 7
			alpha_cnt[S]--; alpha_cnt[E]-= 2; alpha_cnt[V]--; alpha_cnt[N]--;
			cnt[7]++;
		}
		while(alpha_cnt[E]) {	// 9
			alpha_cnt[N]-= 2; alpha_cnt[I]--; alpha_cnt[E]--;
			cnt[9]++;
		}
		printf("Case #%d: ", i);
		for(int j = 0; j <= 9; ++j) {
			while(cnt[j]) {
				printf("%d", j);
				cnt[j]--;
			}
		}
		printf("\n");
	}

	return 0;
}
