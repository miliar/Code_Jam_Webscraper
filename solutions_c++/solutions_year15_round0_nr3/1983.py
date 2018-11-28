#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std;

int l,t,cases=0;
long long x;
char ab[10005];
struct build
{
    int k;
    build(){}
    build(int _k)
    {
        k=_k;
    }
    void d(char xx)
    {
        if(xx=='i')
            k=2;
        else if(xx=='j')
            k=3;
        else
            k=4;
    }
    build operator *(const build &c)const
    {
        if(k==1||k==-1||c.k==1||c.k==-1)
            return build(k*c.k);
        else
        {
            int judge;
            if(k*c.k>0) judge=1;
            else judge=-1;
            int a=k>0?k:-k;
            int b=c.k>0?c.k:-c.k;
            if(a==b)
                return build(-judge);
            else
            {
                if(a==2&&b==3)
                    return build(judge*4);
                if(a==2&&b==4)
                    return build(-judge*3);
                if(a==3&&b==2)
                    return build(-judge*4);
                if(a==3&&b==4)
                    return build(judge*2);
                if(a==4&&b==2)
                    return build(judge*3);
                if(a==4&&b==3)
                    return build(-judge*2);
            }
        }
    }
};
build quickpow(build a, long long n)
{
    build b(1);
    while(n>0)
    {
        if(n&1)
            b=b*a;
        n=n>>1;
        a=a*a;
    }
    return b;
}
int main()
{
    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("fxxk.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&l,&x);
        scanf("%s",ab);
        build a(1),b;
        bool key1=0,key2=0;
        for(int i=0;i<x*l;i++)
        {
            b.d(ab[i%l]);
            a=a*b;
            if(a.k==2)
                key1=1;
            if(key1==1&&a.k==4)
                key2=1;
        }
        build ans=quickpow(a,1);
        if(ans.k==-1&&key1&&key2)
            printf("Case #%d: YES\n",++cases);
        else
            printf("Case #%d: NO\n",++cases);
    }
    return 0;
}
