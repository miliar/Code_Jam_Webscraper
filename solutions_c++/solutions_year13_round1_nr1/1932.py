#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <cmath>
#include <vector>

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

    int64_t T; //number of test cases
    std::vector<int64_t> results; //6 decimal points precision

    while (1) {
        line = getLine();
        if (line.length() == 0 || line == "\n") {
            break;
        }
        {
            stringstream ss(line);
            ss >> T;
            if (T == 0) {
                break;
            }
        }

        double pi = 4 * std::atan(1);
        for (int i = 0; i < T; i++) {
            int64_t r, t;
            line = getLine();
            stringstream ss(line);
            getline(ss, s, ' ');
            stringstream ss2(s);
            ss2 >> r;
            getline(ss, s);
            stringstream ss3(s);
            ss3 >> t;

            int64_t painted = 0;
            r++;
            int rings = 0;
            while (painted < t) {
                painted += 2 * r - 1;
                if (painted > t) {
                    break;
                }
                rings++;
                r += 2;
            }
            results.push_back(rings);
        }
    }

    //std::cout << std::fixed;
    //std::cout << std::setprecision(6);
    //for (std::vector<float>::iterator it = results.begin(); it != results.end(); ++it) {
    //std::cout << "$" << *it << std::endl;
    //}
    int i = 1;
    for (std::vector<int64_t>::iterator it = results.begin(); it != results.end(); ++it) {
        std::cout << "Case #" << i << ": " << *it << std::endl;
        i++;
    }

    if (input) {
        input->close();
        delete input;
    }

    return 0;    
}
