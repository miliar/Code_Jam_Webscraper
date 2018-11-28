#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,t,ca=1;

    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",ca);
        }
        else
        {
            int cur=0;
            long long x=n,ans;
            for(int i=1;;i++)
            {
                long long temp=i;
                temp=temp*x;
                ans=temp;
                while(temp)
                {
                    int tempx=temp%10;
                    temp=temp/10;
                    cur=cur|(1<<(tempx));
                }
                if(cur==1023)
                {
                    printf("Case #%d: %I64d\n",ca,ans);
                    break;
                }
            }
        }
        ca++;
    }
    return 0;
}
