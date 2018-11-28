#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define ss(x) scanf("%s",x)
char st[10000];
int main()
{
    int t,sum,n,i,ans,c=1;
    sd(t);
    while(t--)
    {
        sd(n);
        ss(st);
        sum=0;
        ans=0;
        sum=st[0]-48;
        for(i=1;i<n+1;i++)
        {
            if(sum<i)
            {
                ans++;
                sum+=1;
            }
            sum+=st[i]-48;
        }
        printf("Case #%d: %d\n",c,ans);
        c++;
    }
    return 0;
}
