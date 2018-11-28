#include <iostream>
#include <fstream>
using namespace std;
ifstream in ("snf.in"); ofstream out ("snf.out");
int abs(int x)
{
    if(x<0)return -x;
    return x;
}
int isqrt(int n)
{
    int a = 1;
    int b = n;
    while(abs(a-b)>1)
    {
        b=n/a;
        a=(a+b)/2;
    }
    return a;
}
bool isPal(int n)
{
    int aux = n;
    int og = 0;
    while(aux)
    {
        og=og*10+aux%10;
        aux/=10;
    }
    return (n==og);
}
int main()
{
    int t;
    in >> t;
    for(int cs = 1; cs <= t; cs++)
    {
        int a,b;
        in >> a >> b;
        int sa=isqrt(a);
        int sb=isqrt(b);
        if(sb*sb>b)sb--;
        if(sa*sa<a)sa++;
        int nrFS=0;
        for(int i = sa; i <= sb; i++)
        {
            if(isPal(i))
                if(isPal(i*i))
                    nrFS++;
        }
        out << "Case #" << cs << ": " << nrFS <<'\n';
    }
}
