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
    long long N = stoll(l);
    if (N == 0) return "INSOMNIA";
    long long n;
    valarray<int> f (0,10);
    int k = 0;
    do {
        k += 1;
        n = k * N;
        do {
            int digit = n % 10;
            n /= 10;
            f[digit] = 1;
        } while (n > 0);
    } while (f.sum() != 10);
    return to_string(k*N);
}

int main(int argc, const char * argv[]) {
    string line;
    string path = "/Users/amit/gcj16_q/gcj16_q/";
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

