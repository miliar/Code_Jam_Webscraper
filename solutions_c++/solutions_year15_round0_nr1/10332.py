#include <cstdio>
#include <iostream>

#define ll long long

using namespace std;

char s[1005];

int getInt(char c)
{
    return c-'0';
}

int main()
{
    ll t;
    scanf("%lld",&t);
    
    for (ll tc=1; tc<=t; tc++)
    {
        ll ans=0,current=0,diff=0,len=0;
        
        scanf("%lld",&len);
        scanf("%s",s);
        
        current=getInt(s[0]);
        for (int i=1; i<len+1; i++)
        {
            if (i<current)
            {
                current+=getInt(s[i]);
            }
            else
            {
                diff = i-current;
                ans += diff;
                current+= (diff+getInt(s[i]));
            }
        }
        printf("Case #%lld: %lld\n",tc,ans);
        
    }
    return 0;
}