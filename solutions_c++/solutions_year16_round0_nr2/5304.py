#include <stdio.h>

#define ll long long
int main()
{   ll t,i=0;
    scanf("%lld",&t);
    while(i<t)
    {   char s[1000];
        printf("Case #%lld: ",i+1);
        scanf("%s",s);
        ll x=0,y=0;
        while(s[x]!='\0')
            ++x;
        for(int j=1;j<x;++j)
            if(s[j]!=s[j-1])
                ++y;
        if(s[x-1]=='+')
            printf("%lld\n",y);
        else
            printf("%lld\n",y+1);
        i++;
    }
    return 0;
}