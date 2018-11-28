#include <cstdio>
using namespace std;

int main() {

	FILE * in = fopen("A-large.in", "r");
	FILE * out = fopen("A-large.out", "w");

	int T;

	fscanf(in, "%d", &T);

	for (int c=1; c<=T; c++) {
		int Smax, peopleStand = 0, friends = 0;
		fscanf(in, "%d ", &Smax);
		char S[Smax+1];

		fscanf(in, "%s", S);

		for (int i=0; i<Smax+1; i++) {
			S[i] -= '0';
			if (peopleStand >= i) {
				peopleStand += S[i];
			} else {
				friends += (i - peopleStand);
				peopleStand += (i - peopleStand);
				peopleStand += S[i];
			}
		}

		fprintf(out, "Case #%d: %d\n", c, friends);

	}

	fclose(in);
	fclose(out);

	return 0;
}
