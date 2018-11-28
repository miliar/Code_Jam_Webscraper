#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tt;cin>>tt;
    int q;
    for(int q=1;q<=tt;q++)
    {
    int n,i,j;
    long long k,c,s;
    cin>>k>>c>>s;
    cout<<"Case #"<<q<<": ";
    if(c==1)
    {
        if(k==s)   for(int i=1;i<k+1;i++) cout<<i<<' ';
        else cout<<"IMPOSSIBLE";
        cout<<endl;
    }
    else
    {

        if(c*s<k) { cout<<"IMPOSSIBLE"<<endl; }
        else {  for(int i=0;i<k;i++) cout<<i+1<<' ';
        cout<<endl;}

    }
    }
    return 0;
}
