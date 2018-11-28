#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    int t,ca=1;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",ca++);
        int cur=0;
        int ans[15];
        for(int i=((1<<(n-1))+1);i<(1<<n);i+=2)
        {
            int sign=1;
            for(int j=2;j<11;j++)
            {
                long long temp=1;
                long long num=0;
                for(int k=0;k<n;k++)
                {
                    if(i&(1<<(k)))
                    {
                        num+=temp;
                    }
                    temp=temp*j;
                }
                int flag=0;
                for(int k=2;(long long)k*k<=num;k++)
                {
                    if(num%k==0)
                    {
                      ans[j]=k;
                      flag=1;
                      break;
                    }
                }
                if(flag==0)
                {
                    sign=0;
                    break;
                }
            }
            if(sign==1)
            {
                for(int j=n-1;j>=0;j--)
                {
                    if(i&(1<<j))
                    printf("1");
                    else
                    printf("0");
                }
                for(int j=2;j<11;j++)
                printf(" %d",ans[j]);
                printf("\n");
                cur++;
            }
            if(cur>=m)
            break;
        }
    }
    return 0;
}
