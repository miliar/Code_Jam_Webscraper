#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <fstream>
#include <unordered_map>

using namespace std;

#include "Vector.h"


int main(int argc, const char **argv) {
    // close the iosnyc
    ios::sync_with_stdio(false);
    // file_path
    string file_path = "/Users/lxy/Downloads//";
    string file_name(argv[1]);
    file_path += file_name;
    // open the input file
    fstream file;
    file.open(file_path.c_str());
    /*
    if (file.is_open()) {
        cout<<"open successful!"<<endl;
    }
    else {
        cout<<"open failed!"<<endl;
    }
    */
    // number of the test cases
    int T;
    file >> T;
    vector<string> ret;
    
    while (T > 0) {
        --T;
        // input the X, R, C
        int X, R, C;
        file >> X;
        file >> R;
        file >> C;
        // algorithm
        int sign = 0;
        if (X == 1) {
            sign = 0;
        }
        else if (X > 2 && X / 2 >= min(R, C)) {
            sign = 1;
        }
        else {
            if (R % X == 0 || C % X == 0) {
                sign = 0;
            }
            else {
                sign = 1;
            }
        }

        // collect the results.
        string winner = sign == 0 ? "GABRIEL" : "RICHARD";
        ret.push_back(winner);
    }
    // test the result
    for (int idx = 0; idx < ret.size(); ++idx) {
        cout<<"Case #"<<idx + 1<<": "<<ret[idx];
        if (idx != ret.size() - 1) {
            cout<<endl;
        }
    }
    // close the file
    file.close();
    return 0;
}
