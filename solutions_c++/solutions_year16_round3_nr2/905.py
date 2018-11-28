#include<stdio.h>
#include<iostream>
using namespace std;
long long p[51];
int main()
{
    long long b,m,t,i,k,a[51][51],j,paths,s,bin[55],l,n;
    p[0]=1;
    for(i=1;i<51;i++)
        p[i]=p[i-1]*2;
    //freopen("B-large.in","r",stdin);
    //freopen("outslidelar.txt","w",stdout);
    cin>>t;
    for(k=1;k<=t;k++)
    {
        paths=0;s=0;
        cin>>b>>m;
        for(i=1;i<=b;i++)
        {
            for(j=1;j<=b;j++)
                a[i][j]=0;
        }
        if(m>p[b-2])
            cout<<"Case #"<<k<<": IMPOSSIBLE"<<endl;
        else
        {
            cout<<"Case #"<<k<<": POSSIBLE"<<endl;
            if(m==p[b-2])
            {
                a[1][b]=1;
                m--;
            }
            for(i=0;i<55;i++)
                bin[i]=0;
            l=m;
            for(i=2;l!=0;i++)
            {
                bin[i]=l%2;
                l/=2;
            }
            for(j=2;j<=i;j++)
            {
                if(bin[j]==1)
                {
                    a[j][b]=1;
                    for(l=1;l<j;l++)
                    {
                        for(n=l+1;n<=j;n++)
                            a[l][n]=1;
                    }
                }
            }
            for(i=1;i<=b;i++)
            {
                for(j=1;j<=b;j++)
                    cout<<a[i][j];
                cout<<endl;
            }
        }
    }
    return 0;
}

