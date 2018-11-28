#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B.out");
    int tc = 0;
    fin >> tc;
    for(int ctr = 1;ctr <= tc;ctr++)
    {
            unsigned int a,b,k;
            int ans = 0;
            fin >> a >> b >> k;
            for(unsigned int i = 0;i < a;i++)
            {
                     for(unsigned int j = 0;j < b;j++)
                     {
                              if( (i & j) < k){ ans++;}
                     }
            }
            fout << "Case #" << ctr << ": " << ans << endl;
    }
    return 0;
}
