#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,cases=0;
    scanf("%d",&t);
    while(t--)
    {
        cases++;
        string s;
        int n,i,people=0,ans=0;
        scanf("%d",&n);
        cin>>s;
        for(i=0;i<=n;i++)
        {
            if(s[i]!='0')
            {
                if(people<i)
                {
                    ans+=(i-people);
                    people+=(i-people);
                }
            }
            people+=(s[i]-48);
        }
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
