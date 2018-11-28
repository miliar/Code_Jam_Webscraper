#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;

bool palindrom(long long br) {
    long long rev = 0;
    long long num = br;

    while (num > 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }

    if (rev == br)
        return true;
    else
        return false;
}

long long solve() {
    long long a, b;
    long long ret = 0;

    fin >> a >> b;

    for (long long i=ceil(sqrt(a)); i<=sqrt(b); ++i) {
        if (palindrom(i) && palindrom(i*i)) {
//            cout << i << " " << i * i << endl;
            ret++;
        }
    }

//    cout << endl;
    return ret;
}

int main() {
    int brTest;
    fin.open("fairsquare.in");
    fout.open("fairsquare.out");

    fin >> brTest;

    for (int i=0; i<brTest; ++i) {
        fout << "Case #" << i+1 << ": " << solve() << endl;
    }

    return 0;
}
