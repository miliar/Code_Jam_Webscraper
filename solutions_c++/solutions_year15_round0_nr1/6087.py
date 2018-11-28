#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("c.txt");
    int t, i, j;
    long long s, c;
    char n[10];
    fin>>t;
    if(fin)
    {
    for(j=1; j<=t; j++)
    {
        s=0;
        fin>>n;
        string a;
        fin>>a;
        c=a[0]-48;
        for(i=1; i<a.length(); i++)
        {
            if(c<=i)
            {
                s+=(i-c);
                c+=(i-c);
            }
            c+=(a[i]-48);
        }
        fout<<"Case #"<<j<<": "<<s<<endl;
    }
    }
    return 0;
}
