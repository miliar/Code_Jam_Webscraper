#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

short keys_needed[200];
short total_keys_available[200];
char key_self_accessible_only[200];

short keys[201][200];
short key_to_open_chest[200];
short chest_num_keys[200];
short chest_contains[200][400];
int solution[200];
char is_opened[200];
int K, N;

int branches = 0;

char check_key(int depth) {
	int i, j, k;
	if (depth==N) return 1;	//solution found
	for (i=0; i<N; i++) if (is_opened[i]==0) {
		k = key_to_open_chest[i];
		if (keys[depth][k]) {	//we can open chest i
		//	printf("d %d, i %d, %d %d %d %d\n", depth, i+1, keys[depth][0], keys[depth][1], keys[depth][2], keys[depth][3]);
			keys_needed[k]--;
			solution[depth] = i+1;
			is_opened[i] = 1;
			for (j=0; j<200; j++) keys[depth+1][j] = keys[depth][j];
			keys[depth+1][k]--;
			for (j=0; j<chest_num_keys[i]; j++) keys[depth+1][chest_contains[i][j]]++;
			if (keys[depth+1][k]==0 && keys_needed[k]) {
				//used up last key of type k, but some other chest still needs a type k key to be opened
				if (key_self_accessible_only[k]) {
					is_opened[i] = 0;
					keys_needed[k]++;
					continue;
				}
			}
		//	if (++branches==100000) exit(1);
			if (check_key(depth+1)) return 1;
			is_opened[i] = 0;
			keys_needed[k]++;
		}
	}
	return 0;
}





int main(int argc, char **argv) {
	if (argc!=3) {
		printf("provide input and output file names as command line parameters\n");
	}
	FILE *fp_in, *fp_out;
	if ((fp_in=fopen(argv[1],"r"))==NULL) { printf("can't open file %s\n", argv[1]); exit(1); }
	if ((fp_out=fopen(argv[2],"w"))==NULL) { printf("can't open file %s\n", argv[2]); exit(1); }
	
	int num_cases;
	fscanf(fp_in, "%d\n", &num_cases);
	
	int i, j, k, start_key;
	char ret;
	for (int test_case=1; test_case<=num_cases; test_case++) {
		
		fscanf(fp_in, "%d %d\n", &K, &N);
		printf("test case %d, K %d, N %d\n", test_case, K, N);
		for (i=0; i<200; i++) keys[0][i] = 0;
		for (i=0; i<200; i++) keys_needed[i] = 0;
		for (i=0; i<200; i++) total_keys_available[i] = 0;
		for (i=0; i<200; i++) is_opened[i] = 0;
		for (i=0; i<200; i++) solution[i] = 0;
		for (i=0; i<200; i++) key_self_accessible_only[i] = 1;
		
		for (i=0; i<K; i++) {
			fscanf(fp_in, "%d", &start_key);
			start_key--;	//convert to 0-199 inclusive
			keys[0][start_key]++;
			total_keys_available[start_key]++;
		}
		for (i=0; i<N; i++) {
			fscanf(fp_in, "%hd %hd", &(key_to_open_chest[i]), &(chest_num_keys[i]));
			key_to_open_chest[i]--;
			k = key_to_open_chest[i];
			keys_needed[k]++;
			for (j=0; j<chest_num_keys[i]; j++) {
				fscanf(fp_in, "%d", &start_key);
				start_key--;
				chest_contains[i][j] = start_key;
				total_keys_available[start_key]++;
				if (k!=start_key) 
					key_self_accessible_only[start_key] = 0;	//can gain key "start_key" by having other keys
			}
		}
		
		ret = 1;
		for (i=0; i<200; i++) if (keys_needed[i] > total_keys_available[i]) {
			ret = 0;
		//	printf("prune\n");
		//	printf("i %d, key needed %d, available %d\n", i, keys_needed[i], total_keys_available[i]);
			break;
		}
		if (ret==1) ret = check_key(0);
		
		fprintf(fp_out, "Case #%d:", test_case);
		if (ret==0) fprintf(fp_out, " IMPOSSIBLE\n");
		else {
			for (i=0; i<N; i++) fprintf(fp_out, " %d", solution[i]);
			fprintf(fp_out, "\n");
		}
	}
	
	
	fclose(fp_in);
	fclose(fp_out);
	return 0;
}
