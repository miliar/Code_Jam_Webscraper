#include<bits/stdc++.h>
using namespace std;
bool visit[10];
int n;
void init()
{
    for(int i=0;i<10;i++)
        visit[i]=false;
}
bool ck()
{
    for(int i=0;i<10;i++)
        if(visit[i]==false)
        return false;
    return true;
}
int fun(int nu)
{
    int m=nu;
    while(m!=0)
    {
        visit[m%10]=true;
        m=m/10;
    }
    if(ck()==true)
        return nu;
    else
        fun(nu+n);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("codejam123.out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        init();
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i<<": "<<fun(n)<<endl;
    }
}
