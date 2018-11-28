#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <iomanip>

using namespace std;

int T;
double C, F, X;

void compute(int t, fstream& result){
    long double s = 0;
    double p = 2.0;
    while(1){
        if((X/(p+F) + C/p) > X/p){
            s += X/p;
            break;
        }else{
            s += C/p;
            p += F;
        }
    }
    result << std::fixed;
    result << "Case #" << std::setprecision(7) << t << ": " << s << endl;
}

int main(int argc, char** argv)
{
    std::fstream f;
    std::fstream result;
    result.open("result.txt",std::fstream::out);
    f.open (argv[1], std::fstream::in);

    f >> T;

    for(int t = 1; t <= T; t++){
        f >> C; f >> F; f >> X;
        compute(t,result);
    }

    f.close();
    result.close();
    return 0;
}

