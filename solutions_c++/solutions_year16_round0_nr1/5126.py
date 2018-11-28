#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
using namespace std;


template<typename T>
string to_string(const T& t) {
    ostringstream os;
    os << t;
    return os.str();
}

int main() {
    // Initialization and Input
    ifstream inFile;

    inFile.open("C:\\Users\\Junaid\\Desktop\\CodeBlocks\\cjin.txt");

    int cases;
	inFile >> cases;
    int x;
    int y;
    int count = 0;
    int n = 1;
    int check;
    string str;
    int done = 0;

    vector<int> outputs;
    vector<int> digits;
    for (int i = 0; i < 10; ++i) {
        digits.push_back(i);
    }
    vector<int> digits2 = digits;
    

    for (int i = 0; i < cases; i++) {
        inFile >> x;
        if (x == 0) {
            outputs.push_back(-1);
        } else {
            count = 0;
            done = 0;
            digits = digits2;
            n = 1; 
            while (1) {
                if (done == 1) {
                    break;
                }
                y = x * n;
                str = to_string(y);
                for (int j = 0; j < str.length(); j++) {
                    check = str[j] - '0';
                    if (done == 1) {
                        break;
                    }
                    for (int k = 0; k < 10; k++) {
                        if (check == digits[k]) {
                            digits[k] = -1;
                            count++;
                            if (count == 10) {
                                outputs.push_back(y);
                                done = 1;
                                break;
                            }
                        }
                    }
                }
                n++;
            }
        }
    }

    for (int i = 0; i < cases; ++i) {
        if (outputs[i] == -1) {
            if (i == cases -1) {
                cout << "Case #" << i + 1 << ": INSOMNIA"; 
            } else {
                cout << "Case #" << i + 1 << ": INSOMNIA" << endl; 
            }
        } else {
            if (i == cases -1) {
                cout << "Case #" << i + 1 << ": "  << outputs[i];
            } else {
                cout << "Case #" << i + 1 << ": "  << outputs[i] << endl;
            } 
        }
    }
    return 0;
}
