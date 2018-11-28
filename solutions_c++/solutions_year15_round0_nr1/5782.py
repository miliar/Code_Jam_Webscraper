#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,ans=0,till_now=0;
        char c;
        scanf("%d%c",&n,&c);
        char str[10009];
        scanf("%s",str);
        for(int i=0;i<=n;i++)
        {
            int cnt=str[i]-'0';
            if(till_now>=i)
            {
                till_now+=cnt;
                continue;
            }
            ans+=i-till_now;
            till_now+=i-till_now+cnt;
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
