#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
int main()
{
     freopen("i.txt","r",stdin);
    freopen("output.jjj","w",stdout);
    int i,j,t,n,p,q,r,c,x,m,k,b,u;
    float s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n>>m;
        c=0;
        for(j=n;j<=m;j++)
        {
            r=j;
            b=r;
            k=0;
            while(r)
            {
                k=k*10+(r%10);
                r=r/10;
            }
            if(b==k)
            {
                q=0;
                s=(float)sqrt(k);
                u=sqrt(k);
                x=u;
                if(u==s)
                {
                    while(u)
                    {
                       q=q*10+(u%10);
                       u=u/10;
                    }
                if(q==x)
                c++;
                }
            }
        }
        printf("Case #%d: %d\n",i,c);
    }
}
