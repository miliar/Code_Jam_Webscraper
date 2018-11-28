#include<cstdio>
#include<iostream>
#include<cstring>
#define clr(x) memset(x,0,sizeof(x))
using namespace std;
int a[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;
    scanf("%d",&n);
    int  k,l,ct,m;
    for(int ii=1;ii<=n;ii++)
    {
        clr(a);
        scanf("%d",&k);
        printf("Case #%d: ",ii);
        ct=0;
        m=k;
        if(k==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        while(ct<=9)
        {
            l=k;
            while(l!=0)
            {
                if(a[l%10]==0)
                {
                    a[l%10]=1;
                    ct++;
                }
                l/=10;
            }
            k=k+m;
        }
        k=k-m;
        printf("%d\n",k);
    }
    return 0;
}
