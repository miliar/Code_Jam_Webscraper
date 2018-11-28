#include <iostream>
#include <vector>
#include <cmath>
#include <queue>
#include <fstream>

using namespace std;

ofstream fout ("D.txt");
ifstream fin ("D-small-attempt0.in.txt");

int n, r, c, t;
bool valid;

int solve(int r, int c) {
    
    if(r == 0 || c == 0) {
        return true;
    }
    
    if(r%n == 0 && c >= n-1 && solve(r, c%(n-1))) {
        valid = true;
        return true;
    }
    
    if(r%(n-1) == 0 && c >= n && solve(r, c%n)) {
        valid = true;
        return true;
    }
    
    if(c%n == 0 && r >= n-1 && solve(r%(n-1), c)) {
        valid = true;
        return true;
    }
    
    if(c%(n-1) == 0 && r >= n && solve(r%n, c)) {
        valid = true;
        return true;
    }
    
    if(r%n == 0 && solve(r, c-1)) {
        return true;
    }
    
    if(c%n == 0 && solve(r-1, c)) {
        return true;
    }
    
    return false;
}

int main() {
    
    fin >> t;
    
    for(int i = 0 ; i < t ; i++) {
        fin >> n >> r >> c;
        if(n == 1) {
            fout << "Case #" << (i+1) << ": GABRIEL" << endl;
            continue;
        }
        valid = false;
        if(solve(r,c) && valid)
            fout << "Case #" << (i+1) << ": GABRIEL" << endl;
        else
            fout << "Case #" << (i+1) << ": RICHARD" << endl;

    }
}