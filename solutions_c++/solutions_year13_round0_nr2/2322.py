#include <cstdio>
#include <cstdlib>
using namespace std;

int main(int argc, char **argv) {
	if (argc!=3) {
		printf("provide input and output file names as command line parameters\n");
	}
	FILE *fp_in, *fp_out;
	if ((fp_in=fopen(argv[1],"r"))==NULL) { printf("can't open file %s\n", argv[1]); exit(1); }
	if ((fp_out=fopen(argv[2],"w"))==NULL) { printf("can't open file %s\n", argv[2]); exit(1); }
	
	int num_cases;
	fscanf(fp_in, "%d\n", &num_cases);
	
	int N, M, i, j, k, p, q, height;
	int target[100][100];
	int current[100][100];
	int height_hist[101];
	char impossible;
	for (int test_case=1; test_case<=num_cases; test_case++) {
		fscanf(fp_in, "%d %d\n", &N, &M);
		for (i=0; i<N; i++) {
			for (j=0; j<M; j++) fscanf(fp_in, "%d", &(target[i][j]));
		}
		
		/*
		printf("case %d\n", test_case);
		for (i=0; i<N; i++) {
			for (j=0; j<M; j++) printf("%d ", target[i][j]);
			printf("\n");
		}
		*/
		
		impossible = 0;
		
		for (height=1; height<100; height++) height_hist[height] = 0;
		for (i=0; i<N; i++) for (j=0; j<M; j++) height_hist[target[i][j]] = 1;
		for (i=0; i<N; i++) for (j=0; j<M; j++) current[i][j] = 100;
		
		for (height=1; height<100; height++) if (height_hist[height]) {
			//find a square that must be cut at current height, note the sweeping from lowest to highest
			for (i=0; i<N; i++) for (j=0; j<M; j++) if (target[i][j]==height && current[i][j]>height) {
				//found it, first try to cut going up/down
				for (k=0; k<N; k++) if (target[k][j] > height) break;
				if (k==N) {	//no one is higher, we can cut
					for (p=0; p<N; p++) current[p][j] = height;
				}
				else {
					//try cutting left/right
					for (p=0; p<M; p++) if (target[i][p] > height) break;
					if (p==M) {	//no one is higher, we can cut
						for (q=0; q<M; q++) current[i][q] = height;
					}
					else {
						impossible = 1;
						goto bypass;
					}
				}
			}
		}
		
		bypass:;
		
		fprintf(fp_out, "Case #%d: ", test_case);
		if (impossible) fprintf(fp_out, "NO\n");
		else fprintf(fp_out, "YES\n");
	}
	
	
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
