#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;
int main() {
    ifstream in("A-small-attempt2.in");
    ofstream out("output");
    int T;
    in >> T;
    for(int seq = 1; seq <= T; seq++) {
        long long P,Q;
        char c;
        in >> P >> c >> Q;
        if(Q != 1 && Q % 2) {
            out << "Case #" << seq << ": " << "impossible" << endl;
            continue;
        }
        long long temp = Q;
        while(!(temp % 2)) temp /= 2;
        if(temp > 1) {
            out << "Case #" << seq << ": " << "impossible" << endl;
            continue;
        }
        int i = 0;
        while(pow(2,i) * P < Q) i++;
        out << "Case #" << seq << ": " << i << endl;
    }
    return 0;
}
