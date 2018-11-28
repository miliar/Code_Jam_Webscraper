#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <cmath>
using namespace std;

int b(string s) {
    char last = s[0];
    int ret = 0;
    for (int i = 1; i < s.size(); i++) {
        if (s[i]!=last) {
            last=s[i];
            ret++;
        }
    }
    if (last=='-') ret++;
    return ret;
}

int main() {
    ifstream in("B-large.in");
    ofstream out("b_large.out");
    int n;
    in >> n;
    for (int i = 0; i < n; i++) {
        string s;
        in >> s;
        out << "Case #" << i+1 << ": " << b(s) << endl;
    }
}
