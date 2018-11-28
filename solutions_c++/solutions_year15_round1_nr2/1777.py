#include<stdio.h>
#include<algorithm>
using namespace std;
int arr[1009];
int Barr[1009];
int lcm(int a, int b)
{ return (a/__gcd(a,b))*b; }
int lcms(int b)
{
        int     i, result;
        result = 1;
        for (i = 1; i <=b ; i++)
            result = lcm(result, Barr[i]);
        return result;
}
void min(int *ind,int *minval,int b)
{
    int min,in,i;
    min=arr[1];
    in=1;

    for(i=1;i<=b;i++)
        if(arr[i]<min)
    {
        min=arr[i];
        in=i;
    }
    *ind=in;
    *minval=min;
}
void work(int ntc)
{
    int b,n,i,j,s,lc,indexmin,minval;
    scanf("%d%d",&b,&n);
    for(i=1;i<=b;i++)
    {
        scanf("%d",&Barr[i]);
        arr[i]=0;
    }
    lc=lcms(b);
    //printf("lcm= %d\n",lc);
    s=0;
    for(i=1;i<=b;i++)
        s+=lc/Barr[i];
    if(n>s)
        n=n%s;
if(n==0)
    n=n+s;
    indexmin=0;
    minval=0;
    for(i=1;i<=n;i++)
    {
        min(&indexmin,&minval,b);
        for(j=1;j<=b;j++)
            arr[j]=arr[j]-minval;
        arr[indexmin]=Barr[indexmin];
    }
    printf("Case #%d: %d\n",ntc,indexmin);
}
int main()
{

    #ifndef CODEJAM_OMINO
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    #endif

    int ntc,i;
    scanf("%d",&ntc);
    for(i=1;i<=ntc;i++)
        work(i);
}

