#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

int main()
{
    ifstream in("prob b.in");
    ofstream out("prob b.out");

    int T;
    in >> T;

    for(int t = 0; t < T; ++t) {
        double C, F, X;
        in >> C >> F >> X;
        
        double income = 2;
        double farm_time = 0;
        double time = X/income;
        while(true) {
            farm_time += C/income;
            income += F;
            double new_time = farm_time + X/income;
            if (new_time > time) {
                out << "Case #" << t+1 << ": ";
                out << std::fixed << std::setprecision(7) << time << endl;
                break;
            } 
            else
                time = new_time;    
        }
    }

    out.close();
}
