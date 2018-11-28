#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int flip(string &s, int end) {
    // base condition
    if(end == -1) {
        return 0;
    }

    if(end == 0) {
        return s[end] == '+' ? 0 : 1;
    }

    // split s into two parts A and B
    // characters in B should be all '+'
    int pivot = end;
    while(pivot >= 0 && s[pivot] == '+') {
        --pivot;
    }

    if(pivot == -1) {
        return 0;
    }

    // flip all elements in A
    for(int i = pivot; i >= 0; --i) {
        if(s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }

    // recursively do it for A
    return 1 + flip(s, pivot);
}

int main(int argc, char **argv) {
    int t = 0;
    ifstream f(argv[1]);

    string tmp;
    getline(f, tmp);
    t = atoi(tmp.c_str());

    for(int i = 0; i < t; ++i) {
        string s;
        getline(f, s);
        // cout << "s: " << s << endl;

        cout << "Case #" << i + 1 << ": " << flip(s, s.size() - 1) << endl;
    }

    return 0;
}
