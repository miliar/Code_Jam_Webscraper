#include<bits/stdc++.h>
using namespace std;
int main()
{

    long long int t,i,cnt1=0,cnt2=0,j,n;
    char s[1005];
    scanf("%lld",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%lld",&n);
        cnt1=0;
        cnt2=0;
        scanf("%s",s);
        for(i=1;i<n+1;i++)
        {
            cnt1=cnt1+(s[i-1]-'0');
            if(cnt1<i)
            {
                cnt2=cnt2+(i-cnt1);
                cnt1=cnt1+(i-cnt1);
            }

        }
        printf("Case #%lld: %lld\n",j,cnt2);
    }
    return 0;
}
