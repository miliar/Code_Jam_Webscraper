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
        uint64_t N;
        ifs >> N;
        if (!N) {
            ofs << "INSOMNIA" << endl;
            continue;
        }
        int digits = 0;
        int count = 0;
        while (digits != 0x3ff) {
            ++count;
            digits |= countDigits(count*N);
        }
        ofs << count*N << endl;
    }
    return 0;
}