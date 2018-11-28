#include <iostream>
#include <string>
#include <cctype>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <fstream>
#include <iomanip>
#define in fin
#define out fout
using namespace std;

int main()
{
    unsigned long long T;
    ifstream fin("input.in");
    ofstream fout("output.out");
    in >> T;
    for(unsigned long long tt = 1; tt <= T; tt++) {
        unsigned long long cookies = 0;
        double c, f, x, time = 0;
        double rate = 2, total = 0;
        in >> c >> f >> x;
        double timeToTake = x / rate;
        double mini = timeToTake;
        while(1){
          time = c / rate;
          total += time;
          cookies += rate * time;
          rate += f;
          cookies = 0;
          if(total + x/rate > mini) {
             break;
          }
          else
            mini = min(total + x/rate, mini);
        }
        out << "Case #" << tt << ": "
            << std::fixed << std::setprecision(7) << mini << endl;
    }
    return 0;
}
