#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
using namespace std;
string a,b;
const long long inf = 5000000000000000000ll;
long long ra,rb;
long long abs(long long x)
{
    return x>0?x:-x;
}
void dfs(int now,long long va,long long vb)
{
    if(now==a.length())
    {
        if(abs(va-vb)<abs(ra-rb))
        {
            ra=va,rb=vb;
        }
        else if(abs(va-vb)==abs(ra-rb))
        {
            if(va<ra)
            {
                ra=va;
                rb=vb;
            }
            else if(va==ra&&vb<rb)
            {
                ra=va;
                rb=vb;
            }
        }
        return;
    }
    if(a[now]!='?'&&b[now]!='?')
    {
        va=va*10+a[now]-'0';
        vb=vb*10+b[now]-'0';
        dfs(now+1,va,vb);
        return;
    }
    else if(a[now]=='?'&&b[now]=='?')
    {
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<10;j++)
            {
                dfs(now+1,va*10+i,vb*10+j);
            }
        }
        return;
    }

    if(a[now]!='?')
    {
        va=va*10+a[now]-'0';
    }
    if(b[now]!='?')
    {
        vb=vb*10+b[now]-'0';
    }
    for(int i=0;i<10;i++)
    {
        int ta=va;
        int tb=vb;
        if(a[now]=='?')
        {
            ta=ta*10+i;
            dfs(now+1,ta,tb);
        }
        if(b[now]=='?')
        {
            tb=tb*10+i;
            dfs(now+1,ta,tb);
        }
    }

}
void output(int a,int length)
{
    if(length==0)
    {
        return;
    }
    output(a/10,length-1);
    cout<<a%10;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        cout<<"Case #"<<ti<<": ";


        cin>>a>>b;
        ra=1000;
        rb=-1000;
        dfs(0,0,0);

        output(ra,a.length());
        cout<<' ';
        output(rb,b.length());
        cout<<endl;
    }
    return 0;
}
