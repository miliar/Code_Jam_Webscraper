#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("B-small-attempt0.in");
    int t;
    fin >> t;
    ofstream fout("output.txt");
    for(int s=1; s<=t; ++s)
    {
        int a,b,k;
        int sol=0;
        fin >> a >> b >> k;
        //cout << a << " " << b <<" "<< k << endl;
        for(int i=0; i<a; ++i)
            for(int j=0; j<b; ++j)
            {
                //cout << i << " " << j << " " << (i&j) << endl;
                if((i&j)<k)
                    ++sol;
            }

        //cout << (1&2) << " " << (0&0) << " "<< (1&1) << " "<< (3&2) << " "<< (101&1) << endl;


        fout << "Case #" << s << ": ";

            fout << sol << endl;


    }
}
