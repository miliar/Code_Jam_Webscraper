#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream inf("A-large.in");
    ofstream outf("output.txt");

    int t; inf >> t;
    for (int tt = 1; tt <= t; tt++) {
        outf << "Case #" << tt << ": ";
        int d[10] = {};
        int cnt = 0;
        long long n; inf >> n;
        auto step = n;
        if (n == 0) {
            outf << "INSOMNIA\n";
            continue;
        }
        while (cnt < 10) {
            auto a = n;
            while (a > 0) {
                if (d[a % 10] == 0) {
                    d[a % 10] = 1;
                    ++cnt;
                    if (cnt == 10) {
                        outf << n << "\n";
                    }
                }
                a /= 10;
            }
            n += step;
        }
    }
}