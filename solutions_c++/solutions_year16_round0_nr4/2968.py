#include<bits/stdc++.h>
using namespace std;

int main()
{
    int tt;
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin>>tt;
    for(int t=1;t<=tt;t++)
    {
        long long k,c,s;
        fin>>k>>c>>s;
        fout<<"Case #"<<t<<": ";
        for(int i=1;i<=s;i++)
            fout<<i<<" ";
        fout<<endl;
    }

}
