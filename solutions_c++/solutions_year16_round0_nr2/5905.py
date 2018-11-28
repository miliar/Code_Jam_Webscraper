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
#include <valarray>

using namespace std;

string getNextOut(ifstream& in) {
    string l;
    getline(in,l);
    char c = l[0];
    int n = 0;
    for (char i:l) {
        if (c != i) {
            n++;
        }
        c = i;
    }
    //if (n > 0 && l[0] == '+') n++;
    //else if (n == 0 && l[0] == '-') n++;
    if (l[l.length()-1] == '-') n++;
    return to_string(n);
}

int main(int argc, const char * argv[]) {
    string line;
    string path = "/Users/amit/gcj16_q/gcj16_qB/";
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

