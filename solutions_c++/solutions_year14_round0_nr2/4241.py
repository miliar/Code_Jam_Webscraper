#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream input;
    ofstream output;
    
    input.open(argv[1]);
    output.open("output.out");
    
    int T;
    double C, F, X, R;
    input >> T;
    
    for (int i = 1; i <= T; i++) {
        double time = 0.0;
        input >> C;
        input >> F;
        input >> X;
        R = 2;
        
        while (X/R > C/R + X/(R + F)) {
            time += C/R;
            R = R + F;  
        }
        
        time += X/R;
        
        output << "Case #" << i << ": " << fixed  <<  setprecision(7) << time;
        
        if (i != T)
           output << endl;
    }
}
