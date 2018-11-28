//
//  ProblemA.cpp
//  GCJ2016
//
//  Created by Chelsea Rath on 4/9/16.
//
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

static const string INPUT_FILE = "A_Small.txt";

void readFile(int& testNum, vector<int> tests);
bool computeInsomnoia(int test);
string intToString(int num);

int main() {
    return 0;
}

void readFile(int& testNum, vector<int> tests) {
    ifstream infile(INPUT_FILE);
    
    string line;
    getline(infile, line);
    
    testNum = stoi(line);
    
    while(getline(infile, line)) {
        int number = stoi(line);
        tests.push_back(number);
    }
}

bool computeInsomnoia(int test) {
    string str = intToString(test);
    
    return false;
}

string intToString(int num) {
    stringstream ss;
    ss >> num;
    
    return ss.str();
}