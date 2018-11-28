#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

long long p,q;

void inline scan()
{
    p=q=0;
    bool flip=false;
    int c=getchar();
    for(;(c<47||c>57)&&c!='-';c=getchar());
    //if(c=='-'){neg=1;c=getchar();}
    for(;(c>47 && c<58)||(c=='/');c=getchar())
    {
        if(c=='/'){flip=true;continue;}
        if(!flip){p=(p<<1)+(p<<3)+c-48;}
        else if(flip){q=(q<<1)+(q<<3)+c-48;}
    }
    return;
}


long long gcd(long long p,long long q)
{
    long long temp=0;
    while(p)
    {
        temp=p;
        p=q%p;
        q=temp;
    }

    return q;
}

int main()
{
    freopen("A-large.in" , "r" , stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d",&T);

    for(int t=1;t<=T;t++)
    {
        scan();
        int num=0;int den=0;
        long long g=gcd(p,q);
        p=p/g;
        q=q/g;

        long long x=p;
        long long y=q;
        long long exp;

        while((!(p&1))&&(!(q&1)))
        {
            p=p/2;
            q=q/2;
            num++;
        }

        den=num;
        while((!(q&1)))
        {
            q=q/2;
            den++;
        }

        if((q!=1)||(x>y))
        {
            printf("Case #%d: impossible\n",t);
        }
        else
        {
            exp=pow(2,den-1);
            if(x>=exp){printf("Case #%d: 1\n",t);}
            else
            {
                den=1;
                y=y/2;
                while(x<y)
                {
                    y=y/2;
                    den++;
                }
                printf("Case #%d: %d\n",t,den);
            }
        }

    }

    return 0;
}
