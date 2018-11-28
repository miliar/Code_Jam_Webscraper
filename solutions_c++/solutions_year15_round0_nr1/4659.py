#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int T;
int Smax;
string str;

int main() {
    ofstream fout("A-large.out");
    ifstream fin("A-large.in");
    fin >> T;
    int casenum = 1;
    while (T--) {
        fin >> Smax;
        fin >> str;  // length == Smax + 1
        //
        int res = 0;
        int already = 0;
        for (int i = 0; i <= Smax; i++) {
            if (already >= i) {
                already += str[i] - '0';
            } else {
                int tmp = i - already;
                res += tmp;
                already += tmp;
                already += (str[i] - '0');
            }
        }
        // print
        fout << "Case #" << casenum << ": " << res;
        fout << endl;
        casenum++;
    }
}