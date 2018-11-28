#include <iostream>
#include <stdio.h>
#include <cmath>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("bb.txt");
    int n = 0;

    fin >> n;
    for (int w = 0; w < n; ++w) {
        long long r = 0;
        long long t = 0;
        fin >> r >> t;
        long long ans = 0;

        ans = (long long) ((-2*r+1 + sqrt((2*r-1)*(2*r-1)+8*t))/4);

        fout << "Case #" << w+1 << ": " << ans << endl;
    }



    return 0;
}
