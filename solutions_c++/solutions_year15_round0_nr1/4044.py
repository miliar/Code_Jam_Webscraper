#include <fstream>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ifstream input("A-large.in");
    ofstream output("A-large.out");

    int T, tc = 1;
    input >> T;
    while (T--) {
        int smax;
        input >> smax;
        string ks;
        input >> ks;
        assert(ks.length() == smax+1);

        vector<int> s(ks.begin(), ks.end());
        transform(s.begin(), s.end(), s.begin(),
                  [](const int& v) { return v - '0'; });

        assert(all_of(s.begin(), s.end(), [](const int& v) { return v >= 0 && v < 10; }));

        int y = 0, su = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (su >= i) {
                su += s[i];
            }
            else if (s[i] > 0) {
                int nsu = i - su;
                su += s[i] + nsu;
                y += nsu;
            }
        }

        output << "Case #" << tc++ << ": " << y << endl;
    }
    return 0;
}