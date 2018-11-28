#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
        ifstream input;
        ofstream res;
        int T;
        input.open("inputA");
        res.open("output");
        input >> T;
        for (int i = 0; i < T; i ++) {
                int S;
                int needed = 0;
                int have = 0;
                input >> S;
                string dis;
                input >> dis;
                for (int j = 0; j <= S; j ++) {
                        if (needed + have < j) {
                                needed = j - have;
                        }
                        have = have + (dis[j] - '0');
                }
                res << "Case #" << i + 1 << ": " << needed << endl;
        }
        input.close();
        res.close();
}
