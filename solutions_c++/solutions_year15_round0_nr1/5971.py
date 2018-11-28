#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("output2.txt");
    int t;
    fin >> t;
    for (int o = 1; o <= t; ++o)
    {
        int max = 0, k, sum, n, i;
        char a[1001];
        fin >> n;
        fin.get(a[0]);
        for (int i = 0; i <= n; ++i) fin.get(a[i]);
        for (k = 0; k <= n; ++k)
        {
            sum = 0;
            for (i = 0; i <= k; ++i) sum += a[i] - 48;
            sum = k + 1 - sum;
            if (sum > max) max = sum;
        }
        fout << "Case #" << o << ": " << max << endl;
    }
    fin.close();
    fout.close();

}
