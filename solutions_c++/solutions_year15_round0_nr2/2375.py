#include<fstream>
#include<algorithm>

using namespace std;

ifstream f("B-large.in");
ofstream g("B.out");

int d,v[1005],t,x,z,ans,aux,rez;

int main()
{
    f>>t;
    for(int i=1;i<=t;++i)
    {
        ans=0;
        f>>d;
        for(int j=1;j<=d;++j)
        {
            f>>v[j];
            if(v[j]>ans) ans=v[j];
        }
        rez=ans;
        for(int c=2;c<=rez;++c)
        {
            aux=0;
            for(int j=1;j<=d;++j)
            {
                aux+=(v[j]-1)/c;
            }
            if(aux+c<ans)
                ans=aux+c;
        }
        for(int j=1;j<=d;++j) v[j]=0;
        g<<"Case #"<<i<<": "<<ans<<'\n';
    }
}
