#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <algorithm>
#define N 1000
using namespace std;

char s[10000];
int n;
int T;

int main()
{
    //freopen("test.in","r",stdin);
    //freopen("test.out","w",stdout);

    while(~scanf("%d",&T))
    {
        int ca=1;
        while(T--)
        {
            scanf("%d",&n);
            scanf("%s",s);

            int ans=0;
            ans=s[0]-'0';
            int num=0;

            for(int i=1;i<n+1;i++)
            {
                if(ans>=i)
                ans+=(s[i]-'0');
                else
                {
                    num+=(i-ans);
                    ans+=(i-ans);
                     ans+=(s[i]-'0');
                }
            }

            printf("Case #%d: %d\n",ca++,num);

        }
    }
    return 0;
}
