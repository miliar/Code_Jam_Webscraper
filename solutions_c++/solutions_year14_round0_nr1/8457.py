#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <set>
#include <algorithm>

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
    std::vector<int> results; //6 decimal points precision

    line = getLine();
    {
        stringstream ss(line);
        ss >> T;
    }

    const int guesses = 2;
    const int c = 4;
    for (int i = 0; i < T; i++) {
        int guess[guesses];
        std::set<int> v[guesses][c]; // per each guess per each row

        for (int g = 0; g < guesses; g++) {
            line = getLine();
            stringstream ss(line);
            getline(ss, s);
            stringstream ss1(s);
            ss1 >> guess[g];

            for (int j = 0; j < c; j++) {
                line = getLine();
                stringstream ss(line);
                for (int k = 0; k < c; k++) {
                    if (k == c - 1)
                        getline(ss, s);
                    else
                        getline(ss, s, ' ');
                    stringstream ss2(s);
                    int n;
                    ss2 >> n;
                    v[g][j].insert(n);
                    //std::cout << n << std::endl;
                }
            }
        }

        //std::vector<int> v_intersection;
        //
        //std::set_intersection(v[1][guess[1] - 1].begin(), v[1][guess[1] - 1].end(),
        //v[0][guess[0] - 1].begin(), v[0][guess[0] - 1].end(),
        //std::back_inserter(v_intersection));
        //
        //int intersection = v_intersection.size();

        int intersection = 0;
        int result = 0;
        for (std::set<int>::iterator it=v[0][guess[0] - 1].begin(); it!=v[0][guess[0] - 1].end(); ++it) {
            if (v[1][guess[1] - 1].count(*it)) {
                intersection++;
                if (intersection > 1)
                    break;
                result = *it;
            }
        }

        if (intersection > 1) 
            std::cout << "Case #" << i + 1 << ": " << "Bad magician!" << std::endl;
        else if (intersection == 0) 
            std::cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << std::endl;
        else
            std::cout << "Case #" << i + 1 << ": " << result << std::endl;

    }
    if (input) {
        input->close();
        delete input;
    }

    return 0;    
}
