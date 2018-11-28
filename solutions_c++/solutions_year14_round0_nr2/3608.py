#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <algorithm>
using namespace std;

int main(void){

    ifstream fin("B.in");
    ofstream fout("B.out");
    int n;
    fin>>n;
    fout << std::fixed;
    for(int t = 1; t <= n; t++){
        double c,f,x;
        fin>>c>>f>>x;
        double rate = 2.0000000;
        double time = c/2.0000000;
        while( ((x)/(rate+f)) <= ((x-c)/rate ) ){
            rate += f;
            time += c/rate;
        }
        time += (x-c)/rate;
        fout<<"Case #"<<t<<": "<<std::setprecision(7)<<time<<"\n";

    }
    return 0;
}

