//
//  main.cpp
//  CodeJam.2013.2.A
//
//  Created by Maxim Piskunov on 01.06.2013.
//  Copyright (c) 2013 Maxim Piskunov. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

struct path {
    int o;
    int e;
    int p;
    
    //bool operator<(path right) {
    //    return o < right.o;
    //}
    
    int cost(int N) {
        int n = e - o;
        return (2*n*N + n - n*n)/2;
    }
};

class testCase {
    int N, M;
    vector <path> paths;
    
    long long loss;
    
    void inc(long long cost) {
        loss += cost;
        loss %= 1000002013;
    }
public:
    void solve() {
        //sort(paths.begin(), paths.end());
        
        bool sorted = false;
        while (!sorted) {
            sorted = true;
            for (int i = 0; i < paths.size(); i++) {
                for (int j = 0; j < paths.size(); j++) {
                    if (paths[i].p > 0 && paths[j].p > 0 && paths[i].o > paths[j].o && paths[i].e > paths[j].e && paths[i].o <= paths[j].e) {
                        int pass = min(paths[i].p, paths[j].p);
                        int initCost = paths[i].cost(N) + paths[j].cost(N);
                        path l, s;
                        l.o = min(paths[i].o, paths[j].o);
                        l.e = max(paths[i].e, paths[j].e);
                        s.o = max(paths[i].o, paths[j].o);
                        s.e = min(paths[i].e, paths[j].e);
                        l.p = pass;
                        s.p = pass;
                        int finalCost = l.cost(N) + s.cost(N);
                        inc((long long)(initCost - finalCost) * pass);
                        paths[i].p -= pass;
                        paths[j].p -= pass;
                        paths.push_back(l);
                        paths.push_back(s);
                        sorted = false;
                    }
                }
            }
            /*
            cout << "-------------------------" << endl;
            for (int i = 0; i < paths.size(); i++) {
                if (paths[i].p) {
                    cout << paths[i].o << " " << paths[i].e << " " << paths[i].p << endl;
                }
            }
            */
        }
    }
    
    void read(istream &in) {
        in >> N >> M;
        paths.resize(M);
        for (int i = 0; i < M; i++) {
            in >> paths[i].o >> paths[i].e >> paths[i].p;
        }
    }
    
    void write(ostream &out) {
        out << loss;
    }
    
};

vector <testCase> read() {
    ifstream in("input.txt");
    
    int T;
    in >> T;
    vector <testCase> tests(T);
    for (int i = 0; i < tests.size(); i++) {
        tests[i].read(in);
    }
    
    in.close();
    
    return tests;
}

void write(vector <testCase> tests)
{
    ofstream out("output.txt");
    
    for (int i = 0; i < tests.size(); i++) {
        out << "Case #" << i+1 << ": ";
        tests[i].write(out);
        if (i != tests.size()-1) out << endl;
    }
    
    out.close();
}

void solve(vector <testCase> &tests) {
    for (int i = 0; i < tests.size(); i++) {
        tests[i].solve();
    }
}

int main(int argc, const char * argv[])
{
    vector <testCase> tests = read();
    solve(tests);
    write(tests);
    return 0;
}