#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int singlecase(char const * s, size_t len) {
    int r = 0;
    char chplus = '-';
    char chzero = '+';
    char tmp;
    for (char const * p = s + len - 1; p >= s; --p) {
        if (*p == chplus) {
            ++r;
            tmp = chplus;
            chplus = chzero;
            chzero = tmp;
        }

    }
    return r;
}

int main() {
    string s;
    int numCases = 0;
    getline(cin, s);
    stringstream(s) >> numCases;

    for (int i = 1; i <= numCases; ++i) {
        // read N
        int N = -1;
        getline(cin, s);
        N = singlecase(s.c_str(), s.length());
        cout << "Case #" << i << ": " << N << endl;
    }

}

