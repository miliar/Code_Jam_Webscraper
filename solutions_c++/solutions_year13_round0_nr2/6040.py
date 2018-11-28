#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
 
using namespace std;

char lawn[100][100];
char test[100][100];
int N, M;

void check_horizontal (int pos) {
	int maxval = 0;
	for (int hi = 0; hi < M; ++hi) {
		if (lawn[pos][hi] > maxval) { maxval = lawn[pos][hi]; }
	}
	for (int hi = 0; hi < M; ++hi) {
		if (test[pos][hi] > maxval) { test[pos][hi] = maxval; }
	}
//printf("H%02d:%d, ", pos, maxval);
}

void check_vertical (int pos) {
	int maxval = 0;
	for (int vi = 0; vi < N; ++vi) {
		if (lawn[vi][pos] > maxval) { maxval = lawn[vi][pos]; }
	}
	for (int vi = 0; vi < N; ++vi) {
		if (test[vi][pos] > maxval) { test[vi][pos] = maxval; }
	}
//printf("V%02d:%d, ", pos, maxval);
}

int main(void) {
    int linenum = 0;

	cin >> linenum;

	for (int i = 1; i <= linenum; ++i) {
		string ans = "YES";
		cin >> N >> M;
		for (int ni = 0; ni < N; ++ni) {
			int mi;
			int val;
			for (mi = 0; mi < M; ++mi) {
				cin >> val;
				lawn[ni][mi] = val;
				test[ni][mi] = 100;
//printf("%d,",lawn[ni][mi]);
			}
			lawn[ni][M] = '\0';
			test[ni][M] = '\0';
	    }

		for (int ni = 0; ni < N; ++ni) {
			check_horizontal (ni);
		}
		for (int mi = 0; mi < M; ++mi) {
			check_vertical (mi);
		}
		for (int ni = 0; ni < N; ++ni) {
//for(int mi=0;mi<M;++mi){printf("%d",test[ni][mi]);}printf("\n");
//for(int mi=0;mi<M;++mi){printf("%d",lawn[ni][mi]);}printf("\n");
			if (strcmp(test[ni],lawn[ni])) {
				ans = "NO";
			}
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
    return 0;
}
