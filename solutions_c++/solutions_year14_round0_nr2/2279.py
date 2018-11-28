#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdlib>
#include <iomanip>

double cookie(double c, double f, double x){

    double cps = 2;
    double time = 0;
    double time1 = 0;
    double time2 = 0;

    while(true){

        time1 = x/cps;
        time2 = c/cps + x/(cps+f);

        if(time1 < time2){
           time += time1;
           return time;
        }
        else{
           time += c/cps;
           cps += f;
        }
    }
}

using namespace std;

main(){

    FILE *doc;
    doc = fopen("output.out","w");

    ifstream in;
    in.open("input.in");

    int numOfCases;
    double c, f, x;

    in >> numOfCases;

    for(int t=0; t<numOfCases; t++){
        in >> c;
        in >> f;
        in >> x;

        fprintf(doc, "Case #%d: %.7lf \n",t+1, cookie(c,f,x));
    }
}


