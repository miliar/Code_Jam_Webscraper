#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int i,j,a,b,n,t,d;
    char c[1002],ch;
    freopen("A-large.in","r",stdin);
    freopen("problem-A-output.txt","w",stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>a;
        n=0; b=0;
        for(j=0;j<=a;j++)
        {
            cin>>c[i];
            d=c[i]-'0';
            n+=d;
            if(n==0) b++;
            else n=n-1;
        }
        cout<<"Case #"<<i<<": "<<b<<endl;
    }
    return 0;
}

