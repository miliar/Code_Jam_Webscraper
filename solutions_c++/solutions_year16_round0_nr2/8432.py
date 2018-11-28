#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("Blarg.out", "w", stdout);
    long long int n, i, j, ans;
    scanf("%lld",&n);
    for(i=1; i<=n; i++)
    {
        ans=0;
        string s;
        ans=0;
        char c='+';
        cin>>s;
        for(j=s.size()-1; j>=0; j--)
        {
            if(s[j]!=c)
            {
                ans++;
                if(c=='+')
                {
                    c='-';
                }
                else
                {
                    c='+';
                }
            }
        }
        printf("Case #%lld: %lld\n",i,ans);
    }
    return 0;
}
