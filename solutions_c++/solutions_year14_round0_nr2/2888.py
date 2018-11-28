#include<stdio.h>
#include<stdlib.h>

using namespace std;
#include<set>

int main(int argc, char* argv[]){
    FILE *fin;
    fin = fopen(argv[1], "r");

    int T;
    double C, F, X, time, c_buy, c_sav, income;
    fscanf(fin, " %d ", &T);
    for(int tc=0; tc<T; ++tc){
	C = F = X = 0.0;

	fscanf(fin, " %lf ", &C);
	fscanf(fin, " %lf ", &F);
	fscanf(fin, " %lf ", &X);
//	printf("%f %f %f\n", C, F, X);

	time = 0.0;
	income = 2.0;
	while(true){
	    c_sav = X / income;
	    c_buy = (C / income) + (X / (income + F));
	    if(c_buy < c_sav){
		time += (C / income);
		income += F;
	    }else{
		printf("Case #%d: %.7lf\n", tc+1, time+c_sav);
		break;
	    }
	}
    }
    fclose(fin);

    return 0;
}
