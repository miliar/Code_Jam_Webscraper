#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	FILE *fptr = fopen("A-small-attempt3.in", "r");
	FILE *ffptr = fopen("A-small-attempt3.out", "w");
	int n, a1, a2;
	int array1[5][5], array2[5][5];
	fscanf(fptr,"%d", &n);
	
//	cout << n <<endl<< a1 << endl;
	for (int k=0 ;k < n; k++) {
		fscanf(fptr,"%d", &a1);
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){			fscanf(fptr," %d ", &array1[i][j]);
				cout << array1[i][j] << " ";
			}
			cout << endl;
		}
		fscanf(fptr,"%d", &a2);
		for (int i = 0; i < 4; i++) 
				for (int j = 0; j < 4; j++){
					fscanf(fptr,"%d", &array2[i][j]);
			}
			
		int count = 0;
		int chosen;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if(array1[a1-1][i] == array2[a2-1][j]){
					count++;
					chosen = array1[a1-1][i];
				}					
			}
		}
		if(count == 0){
			cout << "Case #"<<k+1<<": Volunteer cheated!" << endl;
			fprintf(ffptr, "%s", "Case #");
			fprintf(ffptr, "%d", k+1);
			fprintf(ffptr, "%s", ": Volunteer cheated!\n");
			
			
		}else if (count > 1) {
			cout << "Case #"<<k+1<<": Bad magician!" << endl;
			fprintf(ffptr, "%s", "Case #");
			fprintf(ffptr, "%d", k+1);
			fprintf(ffptr, "%s", ": Bad magician!\n");
		}
		else{
			cout << "Case #"<<k+1<<": "<<chosen<< endl;
			fprintf(ffptr, "%s", "Case #");
			fprintf(ffptr, "%d", k+1);
			fprintf(ffptr, "%s", ": ");
			fprintf(ffptr, "%d\n", chosen);
		}
	}
	return 0;
}