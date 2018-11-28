#include<fstream>
using namespace std;
ifstream f("in");
ofstream g("out");
int m,n,J;
unsigned long long c[11];
bool a[33];
unsigned long long ipow(int base,int exp)
{
    unsigned long long result = 1;
    while(exp) { if(exp&1) result*=base;
                 exp>>=1;
                 base*=base;
                 }
    return result;
}
int div(unsigned long long x)
{
    unsigned long long d;
    for(d=2;d*d<=x;++d) if(x%d==0) return d;
    return 0;
}
bool base()
{
    int i,j;
    unsigned long long b;
    for(i=2;i<=10;++i) c[i]=0;
    i=2;
    while(i<=10) { b=0;
                   for(j=1;j<=n;++j) if(a[j]) b+=ipow(i,n-j);
                   c[i]=div(b);
                   if(c[i]) ++i;
                   else i=12;
                   }
    return (i==11);
}
bool gen(int k)
{
    int i;
    if(m==J) return 0;
    if(k==n) { if(base()) { ++m;
                            for(i=1;i<=n;++i) g<<a[i];
                            g<<" ";
                            for(i=2;i<=10;++i) g<<c[i]<<" ";
                            g<<'\n';
                            if(m==J) return 0;
                            }
               }
    else { a[k]=0;
           gen(k+1);
           if(m==J) return 0;
           a[k]=1;
           gen(k+1);
           if(m==J) return 0;
           }
}
int main()
{
    f>>n>>n>>J;
    a[1]=a[n]=1;
    g<<"Case #1:\n";
    gen(2);
    return 0;
}
