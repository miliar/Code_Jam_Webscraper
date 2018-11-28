#include<stdio.h>
#include<iostream>
#include<vector>
#include<string.h>
#include<math.h>


using namespace std;

vector<int> v;

int main() {
	int T, N, t, i, j;
	FILE*f1 = fopen("A-small-attempt1.in", "r+");
	FILE*f2 = fopen("A-small-attempt1.out", "w+");
	long long Q, P;

	int c;
	int a ;
	int b;
	fscanf(f1, "%d", &T);
	double arr[20];

	for (i = 0; i < 20; i++) {
		arr[i] = pow(2, i);

	}


	for (t = 0; t < T; t++) {
		c = 0;
		b = 1;
		a = 1;
		fscanf(f1, "%lld/%lld", &P, &Q);
		fprintf(f2, "Case #%d: ", t + 1);
		
		if (Q % 2 != 0) fprintf(f2, "impossible\n");
		
		else {
			while (P*a <Q) {
				c++;
				a *= 2;
			}
			
			P = P*a -Q;
			while (P % 2 != 0) {
				a = 1;
				while (P*a < Q) a *= 2;
				P = P*a - Q;
			}
			while (Q > a) a *= 2;
			if (Q == a)fprintf(f2, "%d\n", c);

			else if (P == 0) fprintf(f2, "%d\n", c);

			else if (Q%P != 0) fprintf(f2, "impossible\n");

			else fprintf(f2, "%d\n", c);
		}
		

	}

	fclose(f1);
	fclose(f2);

	return 0;
}