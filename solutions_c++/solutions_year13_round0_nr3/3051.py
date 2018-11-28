#include <fstream>
#include <cstring>
#include <cmath>
#include <stdlib.h>
using namespace std;
ifstream f("f.in");
ofstream g("f.out");
unsigned int t,j;
unsigned long long a,b,i,n1,n2,nr;
char s[101],c[101];
short verif(unsigned long long n)
{
    ulltoa(n,s,10);
    strcpy(c,s);
    strrev(c);
    if (strcmp(s,c)==0) return 1;
    else return 0;
}
void rez()
{
    f>>a>>b;
    nr=0;
    n1=(unsigned long long)sqrt(a);
    if ((n1*n1)<a) n1++;
    n2=(unsigned long long)sqrt(b);
    for(i=n1;i<=n2;i++)
    {
        if(verif(i)==1)
        {

            if (verif(i*i)==1) nr++;
        }
    }
}
int main()
{
    f>>t;
    for(j=1;j<=t;j++)
    {
        rez();
        g<<"Case #"<<j<<": "<<nr<<'\n';
    }
    f.close();
    g.close();
    return 0;
}
