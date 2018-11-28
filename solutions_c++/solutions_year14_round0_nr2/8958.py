#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <iomanip>
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

    inFile.open("C:\\Users\\Junaid\\Documents\\Assignment_1\\Assignment1-InputsOutputs\\input\\40.in");
    int cases;
    inFile >> cases;

    double p, q, r;
    vector<double> tempvector;
    vector< vector<double> > games;
    int count = 0;
    for (int i = 0; i < cases; i++) {
        inFile >> p;
        inFile >> q;
        inFile >> r;
        tempvector.push_back(p);
        tempvector.push_back(q);
        tempvector.push_back(r);
        games.push_back(tempvector);
        tempvector = {};
    }
 

    double x, c, f, timer, rate, timea, timeb;
    for (int i = 0; i < cases; i++) {
        c = games[i][0];
        f = games[i][1];
        x = games[i][2];
        timer = 0;
        rate = 2;
        
        while (1) {
            timea = x/rate;
            timeb = c/rate + x/(rate + f);
            if (timea < timeb) {
                timer = timer + timea;
                break;
            } else {
                timer = timer + c/rate;
                rate = rate + f;
            }
        }
        
        cout << fixed;
        if (i != cases - 1) {
            cout << "Case #" << i+1 << ": "<< setprecision(7) << timer << endl;
        } else {
            cout << "Case #" << i+1 << ": "<< setprecision(7) << timer;

        }
    }
    return 0;
}
