#include <iostream>
#include <unistd.h>
#include <cstdio>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]) {
    if(argc != 3) {
        cout << "Usage: " << argv[0] << " <input filename> <output filename>" << endl;
        return 1;
    }
    ifstream in(argv[1]);
    if(!in.is_open()) {
        cout << "Unable to open the file: " << argv[1] << endl;
        return 1;
    }
    ofstream out(argv[2]);
    int T;
    in >> T;
    for(int t = 0; t < T; t++) {
        double C, F, X;
        in >> C >> F >> X;
        double mintime = 1000000.00000;
        for(int i = 0; ;i++) {
            double tokens = 0.00000;
            double rate = 2.000000;
            double time = 0.000000;
            int j = 0;
            while(tokens < X) {
                tokens += rate;
                while(j < i && tokens >= C) {
                    j++;
                    tokens -= C;
                    time += C/rate;
                    rate += F;
                }
            }
            time += X/rate;
            if(mintime > time) {
                mintime = time;
            }
            else {
                out << "Case #" << t+1 << ": ";
                out.unsetf(ios::floatfield);
                out.precision(7);
                out.setf(ios::fixed, ios::floatfield);
                out << mintime << endl;
                break;
            }
        }
    }
    in.close();
    out.close();
    return 1;
}
