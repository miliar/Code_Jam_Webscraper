#include<iostream>
#include<stdio.h>;
#include<cmath>
bool a[1005];
using namespace std;
int main()
{
    freopen("sohel.txt","r",stdin);
    freopen("ahmed.txt","w",stdout);
    int i,sq,x,p,q,k,m,n,t,r;
    for(i=1;i<=1002;i++)
    {
        p=0;q=i;
        while(q)
        {
            p=p*10+q%10;
            q/=10;
        }
        if(p==i)
        {
            r=sqrt(p);
            if(r*r==p)
            {
            x=r;
            sq=0;
            while(x)
            {
                sq=sq*10+x%10;
                x/=10;
            }
            if(sq==r)
            a[i]=1;
          }
        }
    }
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int count=0;
        cin>>m>>n;
        for(i=m;i<=n;i++)
        if(a[i]==1)
        count++;
        cout<<"Case #"<<k<<": "<<count<<endl;
    }
}
