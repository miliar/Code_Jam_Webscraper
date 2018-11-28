#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
struct senate
{
    int n;
    char c;
};
int type,n,total;
senate p[30];
bool comp(senate a,senate b)
{
    if(a.n>b.n)
        return true;
    return false;
}
void baharnikalo()
{
    if(type==2)
    {
        sort(p,p+n,comp);
        while(p[0].n--)
        {
            cout<<p[0].c<<p[1].c<<" ";
        }
    }
    else
    {
        int x;
        sort(p,p+n,comp);
        if(p[0].n>=2)
        {
            total-=2;
            p[0].n-=2;
            if(p[0].n==0)
                type--;
            x=p[0].n>p[1].n?p[0].n:p[1].n;
            if(x>total/2)
            {
                total+=1;
                p[0].n+=1;
                if(p[0].n==1)
                    type++;
                cout<<p[0].c<<" ";
            }
            else
                cout<<p[0].c<<p[0].c<<" ";
        }
        else
        {
            if(type%2==0)
            {
                cout<<p[0].c<<p[1].c<<" ";
                p[0].n--;
                p[1].n--;
                type-=2;
            }
            else
            {
                p[0].n--;
                type--;
                cout<<p[0].c<<" ";
            }
        }
        baharnikalo();
    }
}
int main()
{
    int t,i,k;
    //freopen("A-large.in","r",stdin);
    //freopen("outsenlar.txt","w",stdout);
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        type=n;
        total=0;
        for(i=0;i<n;i++)
        {
            cin>>p[i].n;
            total+=p[i].n;
            p[i].c=i+'A';
        }
        cout<<"Case #"<<k<<": ";
        baharnikalo();
        cout<<endl;
    }
    return 0;
}
