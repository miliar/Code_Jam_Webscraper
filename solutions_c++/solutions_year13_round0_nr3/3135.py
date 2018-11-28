#include <iostream>
#include <fstream>
#include <array>
#include <utility>
#include <vector>
#include <gmp.h>
#include <gmpxx.h>

using namespace std;

string makepal(string suf, bool even) {
    string out(2*suf.size()-(even?0:1), 0);
    int j=0;
    for (int i = suf.size()-1; i >= (even ? 0 : 1); i--) out[j++] = suf[i];
    for (int i = 0; i < suf.size(); i++) out[j++] = suf[i];
    return out;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        cout << "Expected argument\n";
        exit(1);
    }

    ifstream file(argv[1]);
    int ncases;
    file >> ncases;
    for (int i = 0; i < ncases; i++) {
        cout << "Case #" << i + 1 << ": ";
        string from, to;
        file >> from >> to;
        mpz_class a(from, 10), b(to, 10);

        int count = 0;
        ifstream seq("seq.txt");
        while (seq.good()) {
            string pal;
            seq >> pal;
            mpz_class num(pal, 10);
            num *= num;
            if (num.get_str().size() > to.size()) {
                break;
            }
            if (num >= a && num <= b) {
                count++;
            }
        }
        
        cout << count;
        cout << "\n";
    }
}
