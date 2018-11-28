#include <cstring>
#include <cstdlib>
#include <cstdio>

double C,F,X;
int T;
int main() {
	FILE* rfile = fopen("B.in" , "r");
	FILE* wfile = fopen("B-small.out", "w");
	fscanf(rfile,"%d",&T);
	for(int cases=0;cases<T;cases++) {
		fscanf(rfile,"%lf%lf%lf",&C,&F,&X);
		double res = 10000000;
		int numFarms = 0;
		double curT = 0;
		while(X/(numFarms*F+2)>C/(numFarms*F+2)+X/((numFarms+1)*F+2)) {
			curT+=C/(numFarms*F+2);
			numFarms++;
		}
		fprintf(wfile,"Case #%d: %.7lf\n",cases+1,curT+X/(numFarms*F+2));
	}



	fclose(rfile);
	fclose(wfile);
}