#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
	FILE *fptr = fopen("B-large.in", "r");
	FILE *ffptr = fopen("B-large.out", "w");
	int T;
	double C,F,X,prod = 2.0, noFarm, addFarm, time;
	fscanf(fptr, "%d", &T);
	for (int k = 0; k < T; k++) {
		time = 0.0;
		prod = 2.0;
		fscanf(fptr, "%lf %lf %lf", &C, &F, &X);
//		cout << C << " "<<F << " " <<X<<endl;
		while (1) {
			noFarm = X/prod;
			addFarm = C/prod + X/(prod+F); 
			if(addFarm < noFarm){
				time += C/prod;
				prod += F;
			}	
			else{
				time+= X/prod;
				break;
			}
		}
		fprintf(ffptr,"Case #%d: ", k+1);
		fprintf(ffptr,"%.7f\n", time);

		
	}
}