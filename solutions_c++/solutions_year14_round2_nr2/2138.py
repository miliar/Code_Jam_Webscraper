#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
long long a,b,t,k,sol,i,I,j;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>a>>b>>k;
        sol=0;
        for(I=0;I<a;I++)
            for(j=0;j<b;j++)
                if((I&j)<k)
                    sol++;
        cout<<"Case #"<<i<<": ";
        cout<<sol<<'\n';
    }
    return 0;
}
