#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;
int main()
{
    long long int T,S,soln,i,cnt,k;
    char str[1007];
    cin>>T;
    for(k=1;k<=T;k++)
    {
            soln=0;
            scanf("%lld",&S);
            scanf("%s",str);
            cnt=str[0]-'0';
            for(i=1;i<=S;i++)
            {
                if(cnt<i)
                {
                    soln+=(i-cnt);
                    cnt+=(i-cnt);
                }
                cnt+=str[i]-'0';
            }
            printf("Case #%lld: %lld\n",k,soln);
    }
    return 0;
}
