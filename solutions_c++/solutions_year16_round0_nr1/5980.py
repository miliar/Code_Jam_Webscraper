#include<stdio.h>
#include<algorithm>
using namespace std;
int T;
int a[20];
int f()
{
    for(int i=0;i<=9;i++)
    {
        if(a[i]==0)return 0;
    }
    return 1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.txt","w",stdout);
    int i,j,k;
    int p,q,r;
    int t,tt,ttt;
    scanf("%d",&T);
for(int ii=0;ii<T;ii++)
{
    scanf("%d",&k);
    //k=ii;
    r=-1;
    for(i=0;i<12;i++)a[i]=0;
    for(i=1;;i++)
    {
        p=k*i;
        if(p>100000000 || k==0)break;
        while(p!=0)
        {
            a[p%10]++;
            p/=10;
        }
        if(f())
        {
            r=k*i;
            break;
        }
    }
   // if(ii%999 == 0)
    {
    printf("Case #%d: ",ii+1);
    if(r==-1)printf("INSOMNIA\n");
    else printf("%d\n",r);
    }
}

    return 0;
}
