#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

struct node
{
    long long l,r;
}a[10100];

int main()
{
    freopen("1.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long T,cas=0;
    scanf("%I64d",&T);
    while(T--)
    {
        long long fuck=0,cao=0,now=0,i,j,x,n,m,l,r,num,flag,temp;
        scanf("%I64d%I64d",&n,&m);
        for(i=1;i<=m;i++)
        {
            scanf("%I64d%I64d%I64d",&l,&r,&num);
            for(j=now+1;j<=now+num;j++)
            {
                a[j].l=l;
                a[j].r=r;
            }
            now+=num;
        }
        for(i=1;i<=now;i++)
        {
            x=a[i].r-a[i].l-1;
            fuck=fuck+(x*(x+1)/2);
        }
        while(1)
        {
            flag=0;
           // puts("fuck");
            for(i=1;i<=now;i++)
            {
                for(j=1;j<=now;j++)
                {
                    if(i==j)
                        continue;
                    if(a[j].l>a[i].l&&a[j].l<=a[i].r&&a[j].r>a[i].r)
                    {
                        temp=a[j].r;
                        a[j].r=a[i].r;
                        a[i].r=temp;
                        flag=1;
                    }
                }
            }
            if(flag==0)
                break;
        }
        for(i=1;i<=now;i++)
        {
            x=a[i].r-a[i].l-1;
            cao=cao+(x*(x+1)/2);
        }
        printf("Case #%I64d: %I64d\n",++cas,cao-fuck);
    }
    return 0;
}
