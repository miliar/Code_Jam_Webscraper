#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t, S, i, x, y, j;
    char A[1002];
    ifstream infile;
    ofstream outfile;
    infile.open("A-large.in");
    outfile.open("A-large-out.txt");
    infile >> t;
    for(j=1;j<=t;j++)
    {
        infile >> S;
        infile >> A;
        for(i=1, x=A[0]-'0',y=0;i<(S+1);i++)
        {
            if(x>=i)
                x += A[i]-'0';
            else
            {
                if((A[i]-'0')!=0)
                {
                    y += i-x;
                    x = i+(A[i]-'0');
                }
            }
        }
        outfile << "Case #" << j << ": " << y << "\n";
    }
    return 0;
}
