#include<iostream>
using namespace std;
long long t,k,c,s;

unsigned long long pos (long long q, long long w, long long e)
{
    long long p=e;
    for(int o=2; o<=w; o++)
    {
        p=(p-1)*q+e;
    }
    return p;
}

int main()
{
    cin>>t;
    for(int d=1; d<=t; d++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<d<<": ";
        for(int i=1; i<=k; i++)
        {
         cout<<pos(k,c,i)<<" ";
        }
        cout<<endl;
    }

    return 0;
}
