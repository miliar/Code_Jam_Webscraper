//Coded by: speeDemon/thunderclash
#include<bits/stdc++.h>
#define dbg(x)
using namespace std;
typedef long long ll;

inline void invert(char &p)
{
    if(p=='+')
        p='-';
    else
        p='+';
}

int main()
{
    freopen("Bin2.in","r",stdin);
    freopen("Bout.txt","w",stdout);

    ll t,tinit;
    ll len;
    ll i;
    char s[101],polarity;
    ll flips;
    cin>>t;
    tinit = t;
    while(t--)
    {
        flips = 0;
        getchar();  //for newline
        scanf("%s",s);

        polarity = s[0];
        for(i=1;s[i]!='\0';++i)
        {
            if(s[i]!=polarity)
            {
                ++flips;
                invert(polarity);
            }
        }
        if(polarity=='-')
            ++flips;

        printf("Case #%lld: %lld\n",tinit-t,flips);
    }
    return 0;
}
