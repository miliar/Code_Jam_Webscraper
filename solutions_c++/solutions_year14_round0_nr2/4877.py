#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

double solveMinimumCookies(double rate, double C, double F, double X){
    if ((X/rate) <= ((C/rate)+(X/(rate+F)))) return X/rate;
    else return ((C/rate)+solveMinimumCookies(rate+F, C, F, X));
}

int main()
{
    FILE* fin = fopen("B-small-attempt3.in", "r");
    ofstream fout;
    fout.open("output.out");

    int numCases;
    fscanf(fin, "%d\n", &numCases);

    for (int i = 0; i < numCases; i++){
        double rate = 2.0, C, F, X;
        fscanf(fin, "%lf %lf %lf", &C, &F, &X);

        fout.precision(11);
        double solution = solveMinimumCookies(rate, C, F, X);
        fout << "Case #" << i+1 << ": " << solution <<endl;
        }

    fout.close();
    return 0;
}
