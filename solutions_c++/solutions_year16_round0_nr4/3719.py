#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;
int main()
{
    ifstream fin("D-small-attempt2.in");
    ofstream fout("output.out");
    int t;
    fin>>t;
    for(int z=0;z<t;z++)
    {
        int k,c,s,i;
        fin>>k>>c>>s;
        fout<<"Case #"<<(z+1)<<": ";
        for(i=1;i<=k;i++)
            fout<<i<<" ";
        fout<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
