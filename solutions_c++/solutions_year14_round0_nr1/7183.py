// aa.cpp 
#include <iostream>
#include <cstdio>
#define s(n) scanf("%d", &n)

using namespace std;

int magic(int a[][4], int b[][4], int ra, int rb) {
	int count(0); int num;
	for(int j = 0; j < 4; j++) {
		for(int jj = 0; jj < 4; jj++) {
			if(a[ra][j] == b[rb][jj]) {
				count++;
				num = a[ra][j];
			}	
		}
	}

	// cout << count << endl;

	if(count == 0) return 33;		// cheated
	else if(count == 1) return num;	// fair case
	else if(count > 1) return 22;	// bad magician
		
}

int main() {
	int tc; s(tc);
	for(int t = 0; t < tc; t++) {
		int a[4][4], b[4][4], ra, rb;
		s(ra);

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				s(a[i][j]);
			}
		}

		s(rb);
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				s(b[i][j]);
			}
		}

		int d = magic(a, b, ra-1, rb-1);

		if(d >= 1 && d <= 16)
			printf("Case #%d: %d\n", t + 1, d);
		else if(d == 22)
			printf("Case #%d: Bad magician!\n", t + 1);
		else if(d == 33)
			printf("Case #%d: Volunteer cheated!\n", t + 1);

	}

	return 0;
}
