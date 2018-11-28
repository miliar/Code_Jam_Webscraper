#include <bits/stdc++.h>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");

int main()
{
    int t,k,c,s;

    fin>>t;

    for(int i=1;i<=t;i++)
    {
        fin>>k>>c>>s;

        fout<<"Case #"<<i<<": ";
        for(int i=1;i<=k;i++)
            fout<<i<<" ";

        fout<<endl;
    }

    return 0;
}
