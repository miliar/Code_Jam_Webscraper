#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("tryop.txt","w",stdout);
    int t,a[1010];
    cin>>t;
    int m=1,x,r,c;
    while(m<=t)
    {
        cin>>x>>r>>c;
        if((r%x!=0)&&(c%x!=0)) cout<<"Case #"<<m<<": "<<"RICHARD"<<endl;
        else if(r<x-1 || c<x-1) cout<<"Case #"<<m<<": "<<"RICHARD"<<endl;
        else cout<<"Case #"<<m<<": "<<"GABRIEL"<<endl;
        m++;
    }
    return 0;
}
