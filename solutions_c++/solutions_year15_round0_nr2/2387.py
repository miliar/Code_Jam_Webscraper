#include <iostream>
#include <algorithm>
#include<cstdio>
using namespace std;
int calc(int d,int maxim,int A[])
{
    int i,j,count=0,ans=1000000;
    for(i=1;i<=maxim;i++)
        {
            count=0;
            for(j=0;j<d;j++)
            {
                if(A[j]%i==0)
                count+=(A[j]/i)-1;
                else
                {
                    count+=A[j]/i;
                }
            }
            ans=min(ans,count+i);
        }
        return ans;
}
int main()
{
    int t,d,i,j,A[1010],maxim,ans;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d",&d);
        maxim=0;
        for(i=0;i<d;i++)
        {
            scanf("%d",&A[i]);
            maxim=max(maxim,A[i]);
        }
        ans=calc(d,maxim,A);
        printf("Case #%d: %d\n",j,ans);
    }
}
