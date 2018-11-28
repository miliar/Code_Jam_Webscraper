#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,k,c,s;
    ifstream fin("D-small-attempt0.in");
    ofstream fout("out.txt");
    fin>>t;
    for(int j=0;j<t;j++)
    {
        fout<<"Case #"<<j+1<<": ";
        fin>>k>>c>>s;
        for(int i=1;i<=s;i++)
            fout<<i<<" ";
        fout<<"\n";
    }
    return 0;
}
