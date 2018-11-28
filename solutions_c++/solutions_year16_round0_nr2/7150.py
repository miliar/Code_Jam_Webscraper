#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    ll t,T,n,m,i,j,ans;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%lld",&T);
    char s[200],ch;
    for(t=1; t<=T; t++)
    {
        scanf("%s",s);
        n=strlen(s);
        ch='+';
        ans=0;
        for(i=n-1; i>=0; i--)
        {
            if(s[i]!=ch)
            {
                ans++;
                ch=s[i];
            }
        }
        printf("Case #%lld: %lld\n",t,ans);
    }
    return 0;
}

