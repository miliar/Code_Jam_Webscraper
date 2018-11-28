#include<cstdio>
#include<cmath>
#include<stdlib.h>
#include<map>
#include<set>
#include<time.h>
#include<vector>
#include<queue>
#include<string>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define eps 1e-8
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
char str[1005];
int s;
int main()
{
    int cas;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cas);
    for(int c=1;c<=cas;c++)
    {
        int ans=0;
        int tans=0;
        scanf("%d %s",&s,str);
        for(int i=0;str[i];i++)
        {
            if(ans<i)
            {
                tans+=(i-ans);
                ans+=(i-ans);
                ans+=str[i]-'0';
            }
            else
            {
                ans+=str[i]-'0';
            }
        }
        printf("Case #%d: %d\n",c,tans);
    }
    return 0;
}
