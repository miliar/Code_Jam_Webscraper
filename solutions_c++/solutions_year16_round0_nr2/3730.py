#include <cstdio>
#include <iostream>
#include <fstream>
#include <set>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;

void ReversePancake(string &s, int last) {
    for (int i = 0; i <= last; i++) {
        if (s[i] == '+') s[i] = '-';
        else if (s[i] == '-') s[i] = '+';
    }

    reverse(s.begin(), s.begin() + last+1);
}

void solve(ifstream &in, ofstream &out) {
    string s;
    in >> s;
    //cout << s << endl;
    bool unsorted = true;
    int last = s.size() - 1;
    int moves1 = 0, moves2=0;
    while (last>=0) {
        for (int i = last; i >= 0; i--) {
            if (s[i] == '+') last--;
            else break;
        }
        if (last >= 0) moves1++;
        else break;
        if (s[0] == '-'){
            ReversePancake(s,last);
        }
        else {
            int index;
            for (index = 0; index <= last; index++) {
                if (s[index] == '-') break;
            }
            ReversePancake(s, index-1);
        }
        //cout << s << endl;
    }
    cout << moves1 << endl;
    out << moves1 << endl;
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
