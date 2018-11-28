#include <iostream>
#include <iomanip>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
    ifstream in("in.txt");
    if (!in.is_open()) {
        cerr << "File not opened\n";
        return -1;
    }
    int T = 0;
    in >> T;
    for (int i = 0; i < T; i++) {
        double C, F, X;
        in >> C;
        in >> F;
        in >> X;
        double production = 2;
        double time = 0;
        while (true) {
            if (X/production > (X/(production+F) + C/production)) {
                time+=C/production;
                production += F;
            }
            else{
                time+=X/production;
                break;
            }
        }
        cout << "Case #" << i+1 << ": ";
        cout << fixed << setprecision(7) << time;
        cout << endl;

    }
    return 0;
}

