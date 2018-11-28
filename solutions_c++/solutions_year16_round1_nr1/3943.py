//
//  main.cpp
//  gcj16_q
//
//  Created by Amit on 4/9/16.
//  Copyright © 2016 Amit. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <valarray>

using namespace std;

string getNextOut(ifstream& in) {
    string l;
    getline(in,l);
    string ss = "";
    for (char c: l){
        if (c < ss[0]){
            ss = ss + c;
        }
        else ss = c + ss;
    }
    return ss;
}

int main(int argc, const char * argv[]) {
    string line;
    string path = "/Users/amit/gcj16_q/gcj16_1a_a/";
    string infile = path + "in.txt";
    string outfile = path + "out.txt";
    ifstream in(infile);
    if (!in) {
        cout << "\nFile error: " << infile << endl;
        exit(1);
    }
    ofstream out(outfile);
    if (!out) {
        cout << "\nFile error: " << outfile << endl;
        exit(1);
    }
    getline(in,line);
    cout << line <<endl;
    int numCases = stoi(line);
    for (int i = 1; i <= numCases; i++) {
        cout << "\ncase#" << i;
        string sout = getNextOut(in);
        out << "Case #" << i << ":" << " " << sout <<"\n";
    }
    in.close();
    out.close();
    cout << endl;
    return 0;
}

