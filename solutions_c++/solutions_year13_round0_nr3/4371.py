#include <stdio.h>
#include <string.h>

__int64 a[100000];
int n;
__int64 m[50] = {1L,4L,9L,121L,484L,10201L,12321L,14641L,40804L,
44944L,1002001L,1234321L,4008004L,100020001L,102030201L,104060401L,121242121L,
123454321L,125686521L,400080004L,404090404L,10000200001L,10221412201L,
12102420121L,12345654321L,40000800004L,1000002000001L,1002003002001L,1004006004001L,
1020304030201L,1022325232201L,1024348434201L,1210024200121L,1212225222121L,1214428244121L,
1232346432321L,1234567654321L,4000008000004L,4004009004004L};

int judge(char s[])
{
    int i=0, j=strlen(s)-1;
    while(i<j)
    {
        if(s[i]!=s[j])
        {
            return -1;
        }
        i++;j--;
    }
    return 1;
}

void make()
{
    int i;
    __int64 temp;
    char str[20];
    n=0;
    for(i=1;i<10000000;i++)
    {
        sprintf(str,"%d",i);
        if(judge(str)!=1) continue;
        temp = (__int64)i * (__int64)i;
        sprintf(str,"%I64d",temp);
        if(judge(str)==1)
        {
            a[n++]=temp;
            printf("%sL,",str);
        }
    }
}

int erfen(int left, int right, __int64 k)
{
    int middle;
    while(left<right)
    {
        middle = (left + right)>>1;
        if(m[middle]>k) right = middle;
        else if(m[middle]<k) left = middle+1;
        else
            return middle;
    }

    if(left==right) return left;
    if(m[right]>=k) return right;
    return left;
}

int main()
{
    int t, test, i, countm, xx, yy;
    __int64 x, y;
//    freopen("C-large-1.in","r",stdin);
//    freopen("C-large-1.out","w",stdout);

    n=39;
    scanf("%d",&t);
    for(test=1;test<=t;test++)
    {
        scanf("%I64d%I64d",&x, &y);
        xx = erfen(0,39,x);
        yy = erfen(0,39,y);
        countm=yy-xx;
        if(m[yy]==y) countm++;
        printf("Case #%d: %d\n",test,countm);
/*
        for(i=0;m[i]<x && i<39;i++) ;
        countm=0;
        for(;m[i]<=y && i<39;i++) countm++;
        printf("Case #%d: %d\n", test, countm);
        */
    }
    return 0;
}
