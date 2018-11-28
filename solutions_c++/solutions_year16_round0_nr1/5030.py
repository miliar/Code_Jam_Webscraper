#include <fstream>
using namespace std;
ifstream f("in");
ofstream g("out");
int t,i,j,n,a,e[10],m;
bool check(int b)
{
    while(b) { if(!e[b%10]) e[b%10]=1,++m;
               b/=10;
               }
    if(m==10) return 1;
    return 0;
}
int main()
{
    f>>t;
    for(i=1;i<=t;++i) { f>>n;
                        if(!n) g<<"Case #"<<i<<": INSOMNIA"<<'\n';
                        else { a=n;
                               m=0;
                               if(!check(a)) while(!check(a+=n));
                               g<<"Case #"<<i<<": "<<a<<'\n';
                               for(j=0;j<=9;++j) e[j]=0;
                               }
                        }
    return 0;
}
