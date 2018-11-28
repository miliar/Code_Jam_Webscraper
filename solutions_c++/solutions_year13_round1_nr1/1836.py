#include <iostream>
#include <fstream>
#define INPUT "asmall.in"
#define OUTPUT "asmall.out"
using namespace std;

ifstream inf(INPUT, ios::in);
ofstream outf(OUTPUT, ios::out);

void func (int &r, int &t) {
    int ans = 0;
    int count = 0;
    do {
        ans += 2*r + (1 + count*4);
    } while ((ans <= t) && (++count));
    outf << count << endl;
}

int main () {
    int testcase, r, t;

    while (!inf.eof() && inf >> testcase) {
        for (int i=1; i<=testcase; ++i) {
            inf >> r >> t;
            outf << "Case #" << i << ": ";
            func (r, t);
        }
    }
    return 0;
}
