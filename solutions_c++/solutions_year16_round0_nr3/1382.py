#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int work(unsigned n,int radix)
{
    static int prime[10]={2,3,5,7,11,13,17,19,23,29};
    for (int i=0;i<10;++i)
    {
        int remainder=0,j=1;
        unsigned tmp=n;
        for (;tmp;tmp>>=1,j=j*radix%prime[i])
            if (tmp&1)
                remainder=(remainder+j)%prime[i];
        if (remainder==0) return prime[i];
    }
    return 0;
}
void print(unsigned n,int bit)
{
    for (int i=bit-1;i>=0;--i)
        putchar((n&(1u<<i))?'1':'0');
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",cas);
        for (unsigned i=(1u<<(n-1))+1;;i+=2)
        {
            int ans[11];
            bool flag=1;
            for (int j=2;j<=10;++j)
                if ((ans[j]=work(i,j))==0)
                {
                    flag=0;
                    break;
                }
            if (flag)
            {
                print(i,n);
                for (int j=2;j<=10;++j) printf(" %d",ans[j]);
                puts("");
                if (--m==0) break;
            }
        }
    }
    return 0;
}
