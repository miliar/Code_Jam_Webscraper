#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("change.in","r",stdin);
    freopen("out.txt","w",stdout);
    int q,d,n,p;
    int tc,T;
    cin>>T;
    for(tc=1;tc<=T;tc++)
    {
        int x;
        cin>>x;
        q=x/25;
        x=x%25;
        d=x/10;
        x%=10;
        n=x/5;
        p=x%5;
        cout<<tc<<" "<<q<<" QUARTER(S), "<<d<<" DIME(S), "<<n<<" NICKEL(S), "<<p<<" PENNY(S)"<<endl;
    }
}
