#include<stdio.h>
#include<vector>

using namespace std;

int map[4][4];
int map1[4];
int map2[4];

int main()  {
	int t, r1, r2,i,j,k;
	int buf;
	vector<int> v;
	FILE* f = fopen("A-small-attempt.in", "r+");
	FILE*f1 = fopen("A-small-attempt.out", "w+");
	fscanf(f, "%d", &t);
	for (i = 0; i < t; i++){
		fscanf(f, "%d", &r1);
		
		for ( j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				fscanf(f,"%d", &buf);
				if (j == r1-1) map1[k] = buf;
				
			}
		}
		fscanf(f, "%d", &r2);
		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				fscanf(f, "%d", &buf);
				if (j == r2 - 1) map2[k] = buf;
			}
		}
		for (j = 0; j < 4; j++) {
			for (k = 0; k < 4; k++) {
				if (map1[j] == map2[k])v.push_back(map1[j]);
			}
		}
		fprintf(f1,"Case #%d: ", i+1);
		if (v.size() == 1) fprintf(f1,"%d\n", v[0]);
		else if (v.size() == 0) fprintf(f1,"Volunteer cheated!\n");
		else {
			fprintf(f1, "Bad magician!\n");
		}

		v.clear();
	}
	fclose(f);
	fclose(f1);




	return 0;

}

