#include <fstream>
#include <cmath>
using namespace std;
ifstream fin("fair.in");
ofstream fout("fair.out");
long long i,j,n,a,b,rez,ok,aux,k,w;
int v[100000];
double auxd;
int main()
{
    fin>>n;
    for(i=1;i<=n;++i)
        {
            fin>>a>>b;
            rez=0;
            for(j=a;j<=b;++j)
                {
                    auxd=sqrt(double(j));
                    aux=sqrt(j);
                    ok=1;
                    if(aux==auxd)
                        {
                            k=0;
                            while(aux)
                                {
                                    v[++k]=aux%10;
                                    aux=aux/10;
                                }

                    for(w=1;w<=k/2;++w)
                        if(v[w]!=v[k-w+1])
                            ok=0;
                    if(ok==1)
                        {
                            aux=j;
                            k=0;
                            while(aux)
                                {
                                    v[++k]=aux%10;
                                    aux=aux/10;
                                }
                        }
                    for(w=1;w<=k/2;++w)
                        if(v[w]!=v[k-w+1])
                            ok=0;
                    if(ok==1)
                        rez++;
                        }
                }
            fout<<"Case #"<<i<<": "<<rez<<'\n';
        }

    return 0;
}
