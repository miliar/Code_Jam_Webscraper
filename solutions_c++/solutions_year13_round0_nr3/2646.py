#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

bool Fair (int n)
{
     int cs[5];
     int dem = 0;
     while (n > 0)
     {
           cs[dem] = n % 10;
           n = n/10;
           dem = dem + 1;
     }
     for (int i = 0; i < dem; i++)
         if (cs[i] != cs[dem-i-1])
            return false;
     return true;
}
bool Square (int n)
{
     int k = (int) sqrt (n);
     return k*k == n && Fair(k);
}
int main()
{
    ofstream outputfile;
    outputfile.open ("output.txt");
    int t;
    char *inname = "input.txt";
    ifstream infile(inname);
    infile >> t;
    int a,b;
    int rs;
    for (int z = 0; z < t; z++)
    {
        infile >> a;
        infile >> b;
        rs = 0;
        for (int i = a; i <= b; i++)
        if (Fair (i) && Square(i))
        {
           cout << i << "\n";
           rs++;
        }
        outputfile << "Case #" << (z+1) << ": " << rs;
        outputfile << "\n";
    }
    outputfile.close ();
}
