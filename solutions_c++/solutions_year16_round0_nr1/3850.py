#include<bits/stdc++.h>
#include<algorithm>
#define ll long long int
using namespace std;
bool arr[11];
bool check()
{
    int i;
    for(i=0;i<10;i++)
        if(arr[i]==false)
            return true;
    return false;
}
void segregate(ll n)
{
    ll r;
    while(n!=0)
    {
        r=n%10;
        n=n/10;
        arr[r]=true;
    }
}
int main()
{
    ll t,p,n,i,j;
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%lld",&n);
        p=n;
        memset(arr,false,sizeof(bool)*10);
        if(n==0)
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        else
        {
            segregate(p);
            while(check())
            {
                p=p+n;
                segregate(p);
            }
            cout<<"Case #"<<j<<": "<<p<<endl;
        }
    }
    return 0;
}
