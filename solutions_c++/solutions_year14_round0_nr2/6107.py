#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ifstream fin("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.in");
//ofstream fout("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out");
FILE *fout;

int main()
{
    int t;
    fout = fopen("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out", "w");
    fin>>t;
    for (int i=1; i<=t; i++)
    {
        double C,F,X,ans,n;
        fin>>C>>F>>X;
        n = floor((X*1.0-C)/C-2.0/F)+1;
        if (n < 1)
        {
            ans = X/2.0;
        }
        else
        {
            ans = 0.0;
            for (int j=0; j<n; j++)
            {
                ans = ans + C/(2.0+j*F);
            }
            ans = ans + X/(2.0+n*F);
        }
        //fout<<"Case #"<<i<<": ";
        fprintf(fout,"Case #%d: %.7f\n", i, ans);
    }
    fclose(fout);
    return 0;
}
