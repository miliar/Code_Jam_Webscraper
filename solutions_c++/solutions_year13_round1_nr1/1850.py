#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
    int T;
    ifstream fin("1AA-small-attempt0.in");
    ofstream fout("1AA-small-attempt0.out");

    fin >> T;
    int r, t;
    for(int i = 1; i <= T; i++) {
        fin >> r >> t;
        int d = floor(sqrt(t/2));
        while((2*r - 1)*d + 2*d*d > t) d--;
        fout << "Case #" << i << ": " << d << endl;
    }

    return 0;
}
