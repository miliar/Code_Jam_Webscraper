#include <cstdio>
#include <iostream>
using namespace std;

int solveProblem(FILE *f) {
	unsigned int answer, rowPicked[5];
	fscanf(f, "%u", &answer);
	for (unsigned int row = 1; row <= 4; row ++) {
		unsigned int aux;
		if (row == answer) {
			for (int col = 1; col <= 4; col ++) {
				fscanf (f, "%u", &rowPicked[col]);
			}
		}
		else {
			for (int col = 1; col <= 4; col ++) {
				fscanf (f, "%u", &aux);
			}
		}
	}
	
	fscanf(f, "%u", &answer);
	int value = 0;
	for (unsigned int row = 1; row <= 4; row ++) {
                unsigned int aux = 0;
                if (row == answer) {
                        for (int col = 1; col <= 4; col ++) {
                                fscanf (f, "%u", &aux);
				for (int key = 1; key <=4; key++) {
					if (aux == rowPicked[key]) {
						if (value != 0 || value == -1) {
							value = -1;
							break;
						}
						else value = aux;
					}
				}
                        }
                }
                else {
                        for (int col = 1; col <= 4; col ++) {
                                fscanf (f, "%u", &aux);
                        }
                }
        }
	return value;
}

int main (int argc, char** argv) {
	// Open the files
	FILE *f, *g;
	f = fopen("input", "r");
	g = fopen("output", "w");

	unsigned int T;
	fscanf(f, "%u", &T);
	for (unsigned int i = 1; i <= T; i++) {
		int solved = solveProblem(f);
		fprintf(g, "Case #%u: ", i);
		if (solved == -1) 
			fprintf(g, "Bad magician!\n");
		else if (solved == 0)
			fprintf(g, "Volunteer cheated!\n");
		else 
			fprintf(g, "%d\n", solved);
	}
	fclose (f);
	fclose (g);
	return 0;
}
