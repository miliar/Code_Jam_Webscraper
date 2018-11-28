#include<fstream>
#include<cmath>
using namespace std;
ifstream in("fairandsquare.in");
ofstream out("fairandsquare.out");
const long long lim=100000000000000;
long long suma[10000];
bool estePalindrom(long long a)
{
    long long ca=a;
    long long invers=0;
    while(a)
    {
        invers=invers*10+a%10;;
        a/=10;
    }
    if(invers==ca)
        return true;
    return false;
}
void fillEverything(long long lim)
{
    for(long long i=1;i<=sqrt(lim)+10;i++)
    {
        if(estePalindrom(i*i) && estePalindrom(i))
            suma[++suma[0]]=i*i;
    }
}
int main()
{
    long long n;
    long long a, b;
    in>>n;
    fillEverything(lim);
    for(long long i=1;i<=n;i++)
    {
        long long rez=0;
        in>>a>>b;
        for(int j=1;j<=suma[0];j++)
            if(suma[j]>=a && suma[j]<=b)
                rez++;
        out<<"Case #"<<i<<": "<<rez<<"\n";
    }
}
