#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<ctype.h>
 
using namespace std;
 
int imax=100000100,cnt[1001],cnt2[1001],a[10001];
 
int main()
{
    int t,i,j,x,n,s,k,min,p=1;
    scanf("%d",&t);
    p=1;
    while(t--)
    {
        scanf("%d %d",&x,&n);
        for(i=0;i<n;i++) scanf("%d",&a[i]);
        sort(a,a+n);
        s=x;
        k=1;
        for(i=n-1;i>=0;)
        {
            cnt2[i--]=k++;
        }
        k=0;
        if(s==1)
        {
            min=cnt2[0];
        }
        else
        {
        for(i=0;i<n;)
        {
            if(a[i]<s)
            {
                s+=a[i];
                cnt[i]=k;
                i++;
            }
            else
            {
                s=2*s-1;
                k++;
            }
        }
        min=imax;
        for(i=1;i<n;i++)
        {
            if(cnt[i-1]+cnt2[i]<min) min=cnt[i-1]+cnt2[i];
        }
        if(cnt2[0]<min) min=cnt2[0];
        if(cnt[n-1]<min) min=cnt[n-1];
        }
        printf("Case #%d: %d\n",p++,min);
    }
    return 0;
}
