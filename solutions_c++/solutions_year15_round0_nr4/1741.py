#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
//#define fin cin
//#define fout cout
int main()
{
    int T;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>T;
    LL x,r,c;
    for(int t=1;t<=T;t++)
    {
        fout<<"Case #"<<t<<": ";
        fin>>x>>r>>c;
        int f=(r*c)%x;
        if(f==0)
        {
            if((r*c)/x>=x-1)
                fout<<"GABRIEL\n";
            else
                fout<<"RICHARD\n";
        }
        else
            fout<<"RICHARD\n";
    }
    return 0;
}
