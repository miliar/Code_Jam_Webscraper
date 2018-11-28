#include<stdio.h>
#include<stdlib.h>

unsigned long long gen[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001
,1234321ll,4008004ll,100020001ll,102030201ll,104060401ll,121242121ll,123454321ll
,125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll
,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll
,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll
,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll
,100000020000001ll,100220141022001ll,102012040210201ll,102234363432201ll,121000242000121ll
,121242363242121ll,123212464212321ll,123456787654321ll,400000080000004ll};

int bis(unsigned long long p)
{
    int a=0,b=47,mid;
    while(a<b)
    {
        mid = (a+b)/2;
        if (p == gen[mid])return mid;
        if (p < gen[mid])b = mid;
        else a = mid+1;
    }
    return a;
}

int main()
{
    freopen("out3.txt","w",stdout);
    freopen("C-large-1.in","r",stdin);
    int z,t,i,a,b;
    unsigned long long n,m;
    scanf ("%d",&z);
    for (t=1;t<=z;t++)
    {
        scanf ("%llu %llu",&n,&m);
        printf ("Case #%d: ",t);
        a = bis(n);
        b = bis(m);
        if (gen[b]>m)b-=1;
        printf ("%d\n",b-a+1);
    }
    return 0;
}
