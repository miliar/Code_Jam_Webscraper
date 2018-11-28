#include <stdio.h>
#define si(a)   scanf("%d",&a)
int a[5]={1,4,9,121,484};
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int ans,i,T,A,B,CASE=0;
    si(T);
    while(T--)
    {
        si(A);si(B);
        ans=0;
        for(i=0;i<5;i++)
            if(a[i]>=A && a[i]<=B)  ans++;
        printf("Case #%d: %d\n",++CASE,ans);
    }
    return 0;
}
