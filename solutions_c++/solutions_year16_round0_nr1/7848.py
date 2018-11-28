#include <iostream>
#include <fstream>
using namespace std;
ifstream in ("CountingSheep.in");
ofstream out ("CountingSheep.out");
bool nr[11];
bool ver(long long nnou)
{
    while(nnou!=0)
    {
        nr[nnou%10]=1;
        nnou/=10;
    }
    for(int i=0;i<10;i++)
    {
        if(nr[i]==0)
            return 0;
    }
    return 1;
}
void aparite(int n)
{
    long long nnou=0;
    do
    {
        nnou+=n;
    }while(ver(nnou)!=1);
    out<<nnou<<" ";
    for(int i=0;i<10;i++)
    {
        nr[i]=0;
    }
}
int main()
{
    int t,n;
    in>>t;
    for(int i=0;i<t;i++){
        in>>n;
        out<<"Case #"<<i+1<<": ";
        if(n==0)
            out<<"INSOMNIA";
        else
        {
            aparite(n);
        }
        out<<"\n";
    }
    return 0;
}
