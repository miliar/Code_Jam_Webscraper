#include <stdio.h>

void main() {

	int n;
	FILE * f = fopen("in.txt", "r");
	FILE * out = fopen("out.txt", "w");
	fscanf(f, "%d\n", &n);

	for(int i = 0; i < n; i++) {

		int firstAnswer = 0;
		int secondAnswer = 0;
		int ans[16] = {
			1, 1, 1, 1,
			1, 1, 1, 1,
			1, 1, 1, 1,
			1, 1, 1, 1
		};

		fscanf(f, "%d\n", &firstAnswer);

		for(int i = 0; i < 4; i++) {
			int a, b, c, d;
			fscanf(f,"%d %d %d %d\n", &a, &b, &c, &d);
			if( i != firstAnswer - 1) {
				ans[a-1] = 0;
				ans[b-1] = 0;
				ans[c-1] = 0;
				ans[d-1] = 0;
			}
		}

		fscanf(f, "%d\n", &secondAnswer);

		for(int i = 0; i < 4; i++) {
			int a, b, c, d;
			fscanf(f, "%d %d %d %d\n", &a, &b, &c, &d);
			if( i == secondAnswer - 1) continue;			
			ans[a-1] = 0;
			ans[b-1] = 0;
			ans[c-1] = 0;
			ans[d-1] = 0;
		}

		int realAns = -1;
		for(int i = 0; i < 16; i++) {
			if(ans[i] == 1) {
				if(realAns == -1) realAns = i + 1;
				else realAns = -2;
			} 
		}

		if(realAns == -2) fprintf(out, "Case #%d: Bad magician!", i + 1);
		else if(realAns == -1) fprintf(out, "Case #%d: Volunteer cheated!", i + 1);
		else fprintf(out, "Case #%d: %d", i + 1, realAns);

		if(i < n - 1) fprintf(out, "\n");
	}

	fclose(f);
	fclose(out);

}