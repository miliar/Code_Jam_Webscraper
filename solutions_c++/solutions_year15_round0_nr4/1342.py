

#include <cstdio>

// How to count the number of N-ominoes?

using namespace std;

void win(int r) {

	printf("Case #%d: GABRIEL\n", r);
}

void lose(int r ) {
	printf("Case #%d: RICHARD\n", r);

}

void normalize(int &a, int &b);

void normalize(int &a, int &b) {
	if (a < b) {
		a = a + b;
		b = a - b;
		a = a - b;
	}
}


int main(int argc, char const *argv[])
{
	
	int X, R, C, T;
	scanf("%d", &T);

	for(int r = 0; r < T; ++r){
		scanf("%d %d %d", &X, &R, &C);
		if (X >= 7 || (R * C) % X != 0 || (X > R && X > C)) lose(r + 1);
		else {
			normalize(R, C);
			switch(X){
				case 1:
					win(r + 1);
					break;
				case 2:
					win(r + 1);
					break;
				case 3:
					if ((R >= 3) && (C >= 2)) win(r + 1);
					else lose(r + 1);

					break;
					
				default:
					if ((R >= X) && (C >= 3)) win(r + 1);
					else lose(r + 1);
					break;
			}
			
		}
	}


	return 0;
}