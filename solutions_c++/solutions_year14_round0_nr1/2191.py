#include <cstdio>
#include <cstdlib>

int main (int argc, char *argv[]) {
  int T;
  FILE *fin = fopen("in.txt", "r");
  FILE *fout = fopen("out.txt", "w");

  fscanf(fin, "%d", &T);

  for (int i = 0; i < T; i++) {
    int row1[4], row2[4];
    int row1num, row2num;
    fscanf(fin, "%d", &row1num);
    for (int j = 0; j < 4; j++) {
      int temp1, temp2, temp3, temp4;
      fscanf(fin, "%d %d %d %d", &temp1, &temp2, &temp3, &temp4);
      if (j + 1 == row1num) {
        row1[0] = temp1;
        row1[1] = temp2;
        row1[2] = temp3;
        row1[3] = temp4;
      }
    }

    fscanf(fin, "%d", &row2num);
    for (int j = 0; j < 4; j++) {
      int temp1, temp2, temp3, temp4;
      fscanf(fin, "%d %d %d %d", &temp1, &temp2, &temp3, &temp4);
      if (j + 1 == row2num) {
        row2[0] = temp1;
        row2[1] = temp2;
        row2[2] = temp3;
        row2[3] = temp4;
      }
    }
    
    for (int j = 0; j < 4; j++) {
    	printf("%d ", row1[j]);
    }
    printf("\n");
    for (int j = 0; j < 4; j++) {
    	printf("%d ", row2[j]);
    }
    printf("\n");

    int numSame = 0;
    int answer = 0;
    for (int j = 0; j < 4; j++) {
    	for (int k = 0; k < 4; k++) {
    		if (row1[j] == row2[k]) {
    			answer = row1[j];
    			numSame++;
    		}
    	}
    }
    if (numSame == 0) {
    	fprintf(fout, "Case #%d: Volunteer cheated!\n", i + 1);
    } else if (numSame == 1) {
    	fprintf(fout, "Case #%d: %d\n", i + 1, answer);
    } else {
    	fprintf(fout, "Case #%d: Bad magician!\n", i + 1);
    }
  }
}
