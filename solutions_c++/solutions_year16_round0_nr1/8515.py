#include <fstream>
#include <cstring>

using namespace std;

ifstream in ("test.in");
ofstream ou ("test.out");

long long v[10];

int main()
{
    long long x,t,i,q,nr,ul,ok=1,j;
    in>>t;
    for (i=1;i<=t;++i){
        in>>x;
        ou<<"Case #"<<i<<": ";
        if (x==0)
            ou<<"INSOMNIA\n";
        else{
            memset(v,0,sizeof v);
            q=1;
            ok=1;
            while(ok){
                nr=q*x;
                while (nr){
                    ul=nr%10;
                    v[ul]=1;
                    nr/=10;
                }
                ok=0;
                for (j=0;j<=9;++j){
                    if (v[j]==0)
                        ok=1;
                }
                ++q;
            }
            ou<<(q-1)*x<<"\n";
        }

    }
    ou.close();
    return 0;
}
