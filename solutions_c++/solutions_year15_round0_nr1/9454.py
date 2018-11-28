#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main() {
    int t;
    ifstream in("A-large.in");
    ofstream out("A-large.out");
    
    in >> t;

    for (int i = 0; i < t; ++i) {
        int s_max;
        in >> s_max;
        int s[s_max + 1];
        for (int j = 0; j <= s_max; ++j) {
            char c;
            in >> c;
            s[j] = c - '0';
        }
        
        int res = 0;
        int people = s[0];

        for (int j = 1; j <= s_max; ++j) {
            int add = max(0, j - people) * (s[j] != 0);
            res += add;
            people += add + s[j];
        }
        out << "Case #" << i + 1 << ": " << res << endl;
    }
    return 0;
}