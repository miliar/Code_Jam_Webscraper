
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
using namespace std;
ifstream fin("t.in");
ofstream fout("output.txt");
int main()
{
    int t,a,b,cat;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        int sol=0;
        fout<<"Case #"<<i<<": ";
        fin>>a>>b>>cat;
        for(int j=0;j<a;j++)
            for(int k=0;k<b;k++)
            {
                int c=j&k;
                if(c<cat) sol++;
            }
        fout<<sol<<"\n";
    }

}
