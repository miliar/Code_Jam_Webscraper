#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <deque>
#include <iomanip>
using namespace std;

int main()
{
    int T;
    ifstream ifs("input.txt");
    ofstream ofs("out.txt");
    ifs >> T;
    double c,f,x;
    for (int i = 0; i < T; i++) {
        double time = 0.0;
        double income = 2.0;
        ifs>>c>>f>>x;
        while (x / income > (c / income) + x /(income + f) ) {
            time += c / income;
            income += f;
        }
        time += x / income;
        ofs << "Case #" << (i + 1) << ": "<< fixed <<setprecision(7) << time << endl;
    }
}