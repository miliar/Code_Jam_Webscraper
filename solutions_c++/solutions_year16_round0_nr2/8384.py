#include <iostream>
#include <fstream>

using namespace std;

int countDigits(uint64_t N)
{
    int r = 0;
    while (N && r != 0x3ff) {
        r |= 1 << (N % 10);
        N /= 10;
    }
    return r;
}

int main(int argc, char **argv) {
    ifstream ifs;
    ifs.open(argv[1]);
    ofstream ofs;
    ofs.open("result");
    int T;
    ifs >> T;
    for (int c = 1; c <= T; ++c) {
        ofs << "Case #" << c << ": ";
        char s[101];
        ifs >> s;
        int switches = 0;
        int last = 2;
        for (char *sp = s; *sp; ++sp) {
            if (*sp == '+') {
                if (last != 1) ++switches;
                last = 1;
            } else {
                if (last) ++switches;
                last = 0;
            }
        }
        if (last) switches--;
        ofs << switches << endl;
    }
    return 0;
}