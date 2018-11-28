#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long i, j, k, n, y,s, zro, on, to, th, fr, fv, sx, svn, et, nin;
    scanf("%lld",&n);
    for (i=1; i<=n; i++)
    {
        scanf("%lld",&s);
        if(s==0)
        {
            printf("Case #%lld: INSOMNIA\n",i);
        }
        else
        {
            long long p,w = s;
            k = 1;
            zro=1, on=0, to=0, th=0, fr=0, fv =0, sx=0, svn=0, et=0, nin=0;
            for (j=1; j<=100000; j++)
            {
                k = j*w;
                long long x =k;
                while(x!=0)
                {
                    y= x%10;
                    x/=10;
                    if (y==0)
                    {
                        zro=0;
                    }
                    if (y==1)
                    {
                        on =1;
                    }
                    if (y==2)
                    {
                        to=2;
                    }
                    if (y==3)
                    {
                        th=3;
                    }
                    if (y==4)
                    {
                        fr=4;
                    }
                    if (y==5)
                    {
                        fv=5;
                    }
                    if (y==6)
                    {
                        sx=6;
                    }
                    if (y==7)
                    {
                        svn=7;
                    }
                    if (y==8)
                    {
                        et=8;
                    }
                    if (y==9)
                    {
                        nin=9;
                    }
                }
                if(zro==0&&on==1&&to==2&&th==3&&fr==4&&fv==5&&sx==6&&svn==7&&et==8&&nin==9)
                {
                    printf("Case #%lld: %lld\n",i,j*w);
                    break;
                }
            }
        }
    }
}
