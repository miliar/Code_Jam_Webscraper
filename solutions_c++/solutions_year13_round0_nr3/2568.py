#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#define MAXX 10000000
using namespace std;
int a[20],nub,nub2,t,ans;
long long b[1000],aa,bb;
bool check(long long h)
{
        nub=0;
        while(h!=0)
        {
                a[nub]=h%10;
                h/=10;
                nub++;
        }
        for(int i=0;i<nub/2;i++)
        {
                if(a[i]!=a[nub-i-1])
                {
                        return 0;
                }
        }
        return 1;
}
        
main()
{
        freopen("C-large-1.in","r",stdin);
        freopen("outb2.txt","w",stdout);
        for(long long i=1;i<=MAXX;i++)
        {
                if(check(i) && check(i*i))
                {
                        b[nub2]=i*i;
                        nub2++;
                }
        }
        scanf("%d",&t);
        for(int r=1;r<=t;r++)
        {
                ans=0;
                scanf("%I64d %I64d",&aa,&bb);
                for(int i=0;i<nub2;i++)
                {
                        if(b[i]>=aa && b[i]<=bb)
                        {
                                ans++;
                        }
                }
                printf("Case #%d: %d\n",r,ans);
        }
        //system("pause");
}
