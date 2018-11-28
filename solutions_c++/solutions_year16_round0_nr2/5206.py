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

string flipper(string str, int bottom) {
    for (int i = 0; i <= bottom; i++) {
        if (str[i] == '+') {
            str[i] = '-';
        } else if (str[i] == '-') {
            str[i] = '+';
        }
    }
    return str;
}

bool allhappy(string str) {
    bool flag = 1;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '-') {
            flag = 0;
        }
    }
    return flag;
}

int sorter(string pancakes){
    string neworder;
    int steps = 0;

    if (allhappy(pancakes) == true) {
        return 0;
    } else {
        int bottom = 0;
        for (int i = 0; i < pancakes.length(); i++) {
            if (pancakes[i] == '-') {
                bottom = i;
            }
        }
        neworder = flipper(pancakes, bottom);
        steps = 1 + sorter(neworder);
        return steps;
    }

}



int main() {
    // Initialization and Input
    ifstream inFile;

    inFile.open("C:\\Users\\Junaid\\Desktop\\CodeBlocks\\cjin.txt");

    int cases, ans;
	inFile >> cases;
    string x;

    for (int i = 0; i < cases; i++) {
        inFile >> x;
        ans = sorter(x);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
