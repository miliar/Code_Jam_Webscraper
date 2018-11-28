#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <cmath>

using namespace std;

    ifstream input("A-large.in");
    ofstream out("Alarge.out");

void a(string s) {
    deque<char> chars = {s[0]};
    char first = s[0];
    for (int i = 1; i < s.size(); i++) {
        if (s[i]<first) {
            chars.push_back(s[i]);
        } else {
            chars.push_front(s[i]);
            first = s[i];
        }
    }
    for (int i = 0; i < s.size(); i++) {
        out << chars[i];
    }
    out << endl;
}

int main() {
    int n;
    input >> n;
    for (int i = 0; i < n; i++) {
        string s;
        input >> s;
        out << "Case #" << i+1 << ": ";
        a(s);
    }
}
