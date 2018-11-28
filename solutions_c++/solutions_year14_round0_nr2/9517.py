#include <iostream>
#include<algorithm>
#include<fstream>

using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

int t;
long double a,b,c,x,MIN,ans,f;

int main()
{
    fout.precision(7);
    fout<<fixed;
    fin>>t;
    for(int q=1;q<=t;q++)
    {
        fin>>a>>b>>c;
        x=2;
        MIN=c/2;
        f=0;
        while(1)
        {
            ans=MIN;
            f+=a/x;
            x+=b;
            MIN=min(MIN,c/x+f);
            if(max(MIN-ans,ans-MIN)<0.0000001)
                break;
        }
        fout<<"Case #"<<q<<": "<<MIN<<endl;
    }
}
