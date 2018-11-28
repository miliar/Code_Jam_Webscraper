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
#include <bitset>
#include <sstream>

using namespace std;


unsigned long long base2dec(unsigned long long n, int b) {
    //cout << " in base2dec:" << n;
    unsigned long long nb = 0;
    unsigned long long bb = 1;
    do {
        nb += n % 10 * bb;
        bb *= b;
        n /= 10;
    } while (n > 0);
    return nb;
}

unsigned long getDiv(unsigned long long n) {
    //cout << " in getdiv:" << n;
    for (unsigned long i=2; i<sqrt(n); i++) {
        if (n % i == 0) {
            //cout <<"\n"<<n << " "<<i;
            return i;
        }
    }
    return 0;
}

string getNextOut(ifstream& in, ofstream& out) {
    string l;
    getline(in,l);
    stringstream ss(l);
    unsigned long d[9];
    //long long sn = 1000000000000001;
    //long long ln = 1111111111111111;
    string stb;
    getline(ss,stb,' ');
    const int nbits = 16;
    unsigned long long sn = pow(2, nbits-1) + 1;
    unsigned long long ln = pow(2, nbits) - 1;
    
    getline(ss,stb,' ');
    int j = stoi(stb);
    //cout << "\nj:" << j;
    
    
    while (sn <= ln && j>0) {
        bitset<nbits> a(sn);
        cout<<"\nb:" <<a;
        int f = 1;
        for (int i = 2; i<11; i++) {
            //cout<<"\ni: "<<i<<" sn: "<<sn;
            //cout<<" b:" <<a;
            d[i-2] = getDiv(base2dec(stoll(a.to_string()), i));
            if (d[i-2] == 0) {
                f = 0;
                break;
            }
        }
        if (f) {
            //cout <<"\nch:" << sn;
            out << a;
            for (auto& di : d) {
                out << " " << di;
            }
            out << "\n";
            cout << "\nj:" << j;
            j--;
        }
        sn += 2;
    }
    return "done";
}

int main(int argc, const char * argv[]) {
    string line;
    string path = "/Users/amit/gcj16_q/gcj16_qC/";
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
        out << "Case #" << i << ":" << "\n";
        string sout = getNextOut(in, out);
        cout << "\ncase#" << i;
    }
    in.close();
    out.close();
    cout << endl;
    return 0;
}

