#include <algorithm>
#include <string>
#include <iostream>
#include <cstdio>
using namespace std;
long long a[100007];
bool isok()
{
    for(int i=0; i<10; i++)
    {
        if(a[i]==0) return false;
    }
    return true;
}
void haha(int numm)
{
    while(numm)
    {
        int we=numm%10;
        numm/=10;
        a[we]=1;
    }
}
int main()
{
    freopen("A-small-attempt3.in", "r", stdin);
    freopen("A-small-attempt3.out", "w", stdout);
    int t;
    cin>>t;
    long long n;
    int flag=0;
    for(int er=1; er<=t; er++)
    {
        flag=0;
        for(int i=0; i<10; i++) a[i]=0;
        cin>>n;
        long long ad=n;
        for(int i=0; i<500000; i++)
        {
            haha(n);
            if(isok())
            {
                cout<<"Case"<<' '<<'#'<<er<<':'<<' '<<n<<endl;
                flag=1;
                break;
            }
            n+=ad;
        }
        if(flag==0)cout<<"Case"<<' '<<'#'<<er<<':'<<' '<<"INSOMNIA"<<endl;
    }
    return 0;
}
