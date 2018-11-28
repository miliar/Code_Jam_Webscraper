#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <cmath>

using namespace std;

//Google Codejam 2013

ifstream *input;
string getLine() {
    string line;
    if (input)
        getline(*input, line);
    else
        getline(std::cin, line);
    return line;
}

int main (int argc, char * argv[]) {
    string s, line;
    if (argc > 1) {
        input = new ifstream(argv[1], std::ios_base::in);
        if (!input->good()) {
            return -1;
        }
    }

    int T; //number of test cases

    line = getLine();
    {
        stringstream ss(line);
        ss >> T;
    }

    double C, F, X;

    for (int i = 0; i < T; i++) {
        line = getLine();
        stringstream ss(line);
        getline(ss, s, ' ');
        stringstream ss1(s);
        ss1 >> C;
        getline(ss, s, ' ');
        stringstream ss2(s);
        ss2 >> F;
        getline(ss, s);
        stringstream ss3(s);
        ss3 >> X;

        int farms = std::max(0, (int)std::ceil((F * X - F * C - 2 * C) / (F * C)));

        double timeSum = 0;
        for (int f = 0; f < farms; f++) {
            timeSum += 1 / (2 + f * F);
        }
        timeSum *= C;

        timeSum += X / (2 + farms * F);

        std::cout << std::setprecision(20) << "Case #" << i + 1 << ": " << timeSum << std::endl;
    }

    if (input) {
        input->close();
        delete input;
    }

    return 0;    
}
