#include <fstream>
using namespace std;

ifstream f("i.in");
ofstream g("o.out");

int a[6]={0,2,4,9,121,484};

int main()
{
    int t,i,j,nr,x,y;
    f>>t;
    for(i=1;i<=t;++i)
    {
        f>>x>>y;
        nr=0;
        for(j=0;j<6;++j)
        {
            if(a[j]>=x&&a[j]<=y) nr++;
        }
        g<<"Case #"<<i<<": "<<nr<<'\n';
    }
    f.close();
    g.close();
    return 0;
}
