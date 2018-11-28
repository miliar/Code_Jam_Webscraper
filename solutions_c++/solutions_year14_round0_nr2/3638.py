#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    double c,f,x,ans,tmp;
    int i,j,k,n,t;
    fin>>t;
    for (k=1; k<=t; k++)
    {
        fin>>c>>f>>x;
        n=(x*f-2*c)/(c*f);
        ans=c/2.0;
        for (i=1; i<=n-1; i++)
            ans+=(c/(2+i*f));
        ans+=(x/(2+n*f));
        if (ans>(x/2.0)) ans=x/2.0;
        fout<<"Case #"<<k<<": "<<fixed<<setprecision(7)<<ans<<endl;
    }
    return 0;
}
