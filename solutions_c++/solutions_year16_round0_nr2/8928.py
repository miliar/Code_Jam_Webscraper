#include <bits/stdc++.h>
#define ll long long

using namespace std;
int main()
{

    int t,d=0;
    scanf("%d",&t);
    while(t--)
    {
        d++;

        char str[105];
        scanf("%s",str);
        ll n=strlen(str);
        ll cn=0,st=0;
        if(str[0]=='+')
            st=1;
        for(ll i=1;i<n;i++)
        {
            if(str[i]!=str[i-1])
            {
                st=1-st;
                cn++;

            }
        }
        if(st==0)
            cn++;

        printf("Case #%d: %lld\n",d,cn);

    }
    return 0;
}
