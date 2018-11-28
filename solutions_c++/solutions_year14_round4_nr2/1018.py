#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const int M=5010;
int sec[M];
int n;

int main()
{
//    freopen("in.txt","r",stdin);
    while(scanf("%d",&n)==1)
    {
        int i,j;
        int ans,sum=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&sec[i]);
            for(j=i-1;j>=0;j--)
                if(sec[j]>sec[i])
                    sum++;
        }
        ans=sum;
        for(i=0;i<n;i++)
        {
            sum=sum-sec[i]+(n-1-sec[i]);
            if(ans>sum)
                ans=sum;
        }
        printf("%d\n",ans);
    }
    return 0;
}
