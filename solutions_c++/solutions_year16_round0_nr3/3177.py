#include <cstdio>
#include <iostream>
#include <fstream>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#define N 14
int solutions = 0;
using namespace std;

void solve(ifstream &in, ofstream &out) {
    int K, C, S;
    in >> K >> C >> S;
    for (int i = 1; i < S; i++)
        out << i << " ";
    out << S << endl;
}

int main() {
    ifstream in("A.in");
    ofstream out("A.txt");
    int T;
    in >> T;
    for (int i = 1; i <= T; i++){
        out << "Case #" << i << ": ";
        cout << "Case #" << i << ": ";
        solve(in, out);
    }
    return 0;
}
