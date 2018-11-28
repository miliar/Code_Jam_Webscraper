#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>

using namespace std;

const int max_n = 10002;

ifstream fin("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.in");
//ofstream fout("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out");
FILE *fout;

int s[max_n];

int main()
{
    fout = fopen("/Users/sukixia/Documents/c_plus_plus/CodingTest/CodingTest/file.out", "w");
    int t;
    int n,x,i;
    
    fin>>t;
    for (i=1; i<=t; i++)
    {
        int j,k,m;
        int bp;
        
        fin>>n>>x;
        for (j=0; j<n; j++)
            fin>>s[j];
        sort(s,s+n);
        m = 0;
        bp = n-1;
        for (j=0; j<n; j++)
        {
            while (bp>j)
            {
                if ((s[bp]+s[j])<=x)
                {
                    m++;
                    bp--;
                    break;
                }
                bp--;
            }
        }
        fprintf(fout, "Case #%d: %d\n", i, n-m);
    }
    fclose(fout);
    return 0;
}