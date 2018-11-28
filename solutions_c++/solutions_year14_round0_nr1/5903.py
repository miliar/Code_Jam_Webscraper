#include <iostream>
#include <fstream>

using namespace std;

void go (int t) {
	printf ("Case #%d: ", t);
	int mask [2] = {0,0};
	int x;
	for (int i = 0; i < 2; i ++) {
		int m; cin >> m;
		for (int j =0 ; j < 4; j++){
			for (int k = 0; k < 4; k ++) {
				cin >> x;
				if (j == m - 1)
					mask [i] |= (1 << x);
			}
		}
	}
	int res = mask [0] & mask [1];
	if (res == 0) {
		printf ("Volunteer cheated!\n");
	}else if ((res & (res - 1)) != 0) {
		printf ("Bad magician!\n");
	}else {
		for (int i = 0; i<=16; i ++) {
			if (res == (1 << i)) {
				printf ("%d\n", i);
				break;
			}
		}
	}
}

int main () {
	int N;
	cin >> N;
	for (int i = 0; i < N; i ++) {
		go (i + 1);
	}
}
