#include<bits/stdc++.h>
using namespace std;
#define cin(n) scanf("%d",&n)
#define cinl(n) scanf("%lld",&n)

int a[207],v[207];
long long min(long long a,long long b)
{
    return a<=b?a:b;
}
int main()
{
    int x,t,m,n,i,j,k,l;
    int ct=1;
    cin(t);

    while(t--)
    {
        memset(a,0,sizeof(a));
        memset(v,0,sizeof(v));
        cin(x);
        cin(m);
        cin(n);

        if(m>n)
            swap(m,n);



        int ans=0;
        int z=x;




        x-=m;
        for(i=1;i<=n;i++)
        {
            for(j=0;j<=x/2;j++)
            {
                int fg=0,gg=0,co=0;
                int vl=(i-1)*m;
                int vl2=(n-i)*m;


                vl-=j;
                vl2-=(x-j);
                if((vl>0&&vl2>0)&&(vl%z||vl2%z))
                    fg++;

                if(vl<0||vl2<0)
                {}
                else
                {
                    co++;
                    gg=1;
                    v[j]++;
                }

                vl=vl+j-(x-j);
                vl2=vl2+(x-j)-j;
                if((vl>0&&vl2>0)&&(vl%z||vl2%z))
                    fg++;

                if(vl>0&&vl2>0)
                    co++;

                if(vl<0||vl2<0)
                    {}
                else if(!gg)
                    v[j]++;
                else{}

                if(fg==co&&co>0)
                    a[j]++;
            }
        }
        for(i=0;i<=x/2;i++)
        {
            if(v[i]>0&&a[i]==v[i])
                ans=1;
           //cout<<i<<" "<<a[i]<<" "<<v[i]<<"\n";
        }
        if(x<0)
            ans=0;

        if((m*n)%z!=0)
            ans=1;

        int aa=m+1;
        int b=z-aa;

        if(aa>0&&b>=0)
        {
            if(b>=m||aa>n)
                ans=1;
        }

        if(z>n)
            ans=1;

        cout<<"Case #"<<ct++<<": ";
        if(ans)
            cout<<"RICHARD\n";
        else
            cout<<"GABRIEL\n";

    }

    return 0;
}
