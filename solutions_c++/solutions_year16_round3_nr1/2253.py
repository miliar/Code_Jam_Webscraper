//
//  main.cpp
//  gcj16_1c1
//
//  Created by Amit on 5/8/16.
//  Copyright © 2016 Amit. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <string>
#include <valarray>
#include <bitset>
#include <sstream>
#include <climits>
#include <vector>
#include <algorithm>

using namespace std;



string getNextOut(ifstream& in, ofstream& out) {
    //string l;
    //getline(in,l);
    stringstream o;
    int n,k;
    in >> n;
    char l = 'A';
    vector<pair<int, char>> a;
    for (int i=0;i<n;i++) {
        in >> k;
        a.push_back(make_pair(k, l+i));
        cout<< "\n" << a[i].first << " " << a[i].second;
    }
    while (a.size()>2) {
        sort(a.rbegin(), a.rend());
        int t = a[0].first - a[1].first;
        if (a[0].first == 1) {
            o << " " << a[0].second;
            a[0].first--;
        }
        else if (t==0) {
            o << " " << a[0].second << a[1].second;
            a[0].first--;
            a[1].first--;
        }
        else {
            for (int i=0;i<t/2;i++) {
                o << " " << a[0].second << a[0].second;
                a[0].first -= 2;
            }
            if (t%2 == 1) {
                o << " " << a[0].second;
                a[0].first -= 1;
            }
        }
        if (a[0].first == 0) {
            a.erase(a.begin());
        }
        //cout << "\n" << o.str();
    }
    while(a[0].first) {
        o << " " << a[0].second << a[1].second;
        a[0].first--;
        a[1].first--;
    }
    return o.str();
}

int main(int argc, const char * argv[]) {
    string line;
    string path = "/Users/amit/gcj16_q/gcj16_1c1/";
    string infile = path + "in.txt";
    string outfile = path + "out1.txt";
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
        string sout = getNextOut(in, out);
        cout << "\ncase#" << i;
        out << "Case #" << i << ":" << sout << "\n";
    }
    in.close();
    out.close();
    cout << endl;
    return 0;
}

