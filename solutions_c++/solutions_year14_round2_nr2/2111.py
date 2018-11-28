#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iomanip>
using namespace std;
typedef long long int LL;

//#define fin cin
//#define fout cout
int main()
{
    ios_base::sync_with_stdio(0);
    LL t,a,b,k;
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");
    fin>>t;
    for(LL n=1;n<=t;++n)
    {
        fin>>a>>b>>k;
        LL ans=0;
        for(LL i=0;i<a;++i)
        {
            for(LL j=0;j<b;++j)
            {
                if((i&j)<k)ans++;
                //fout<<(i&j)<<endl;
            }
        }
        fout<<"Case #"<<n<<": "<<ans<<endl;
    }
    return 0;
}
