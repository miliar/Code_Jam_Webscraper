#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std;
int n,t,r;
int use[10];
bool notfull()
{
    int p=r;
    while(p)
    {
        use[p%10]=1;
        p/=10;
    }
    for(int i=0;i<=9;i++)
        if(!use[i])
        return true;
    return false;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    cin>>t;
    for(int o=1;o<=t;o++)
    {
        cin>>n;
        memset(use,0,sizeof(use));
        if(!n)
        {
            cout<<"Case #"<<o<<": INSOMNIA"<<endl;
            continue;
        }
        r=n;
        while(notfull())
            r+=n;
        cout<<"Case #"<<o<<": "<<r<<endl;
    }
    return 0;
}
