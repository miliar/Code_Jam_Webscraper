#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
int main()
{

    ifstream fin("input.in");
    ofstream fout("output.txt");

    int testcase;
    fin>>testcase;
    for(int test=1;test<=testcase;test++)
    {

        fout<<"Case #"<<test<<": ";

        LL k,c,s;

        fin>>k>>c>>s;



        for(int i=1;i<=k;i++)
            fout<<i<<" ";
        fout<<endl;
    }

}
