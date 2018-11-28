#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream in("A-large.in");
ofstream out("output.in");

int main() {
    int S, T;
    in >> T;
    string str;
    for (int k = 1; k <= T; k ++) {
        in >> S >> str;
        int num = 0, res = 0;
        for (int i = 0; i <= S; i ++) {
            int r = str[i] - '0';
            if (res < i && r != 0) {
                num += (i - res);
                res += (i - res);
            }
            res = res + r;
            //res = res + r + (i - res);
        }
        out << "Case #" << k << ": " << num << endl;
    }
    return 0;
}