#include<bits/stdc++.h>
using namespace std;
long long power(long long n,long long k)
{
    if(k==0)
        return 1;
    long long temp=power(n,k/2);
    temp=temp*temp;
    if(k&1)
        temp*=n;
    return temp;
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("opd.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
    long long int k,c,s;
    cin>>k>>c>>s;
    int i;
    long long val=power(k,c-1),ind=1;
    cout<<"Case #"<<z<<": ";
    for(i=0;i<k;i++)
    {
        cout<<ind<<" ";
        ind+=val;
    }
    cout<<endl;
    }
    return 0;
}
