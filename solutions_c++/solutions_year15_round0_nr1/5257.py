#include<bits/stdc++.h>
using namespace std;
string a;
int main()
{
    int t,t2=0;
    cin>>t;
    while(t--)
    {
        t2++;
        int i,n;
        cin>>n;
        cin>>a;
        int curr=0,req=0,mx=0;
        for(i=0; i<=n; i++)
        {
            req=i-curr;
            if(req>mx)mx=req;
            curr+=(a[i]-'0');
        }
        cout<<"Case #"<<t2<<": "<<mx<<endl;
    }
    return 0;
}
