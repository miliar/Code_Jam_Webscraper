#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int T,l,cases=0;
char k[5005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("fxxk.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&l);
        scanf("%s",k);
        int pos=0,top=0,ans=0;
        while(pos<l)
        {
            top+=k[pos]-'0';
            pos++;
            if(pos>top)
            {
                ans++;
                top++;
            }
        }
        printf("Case #%d: %d\n",++cases,ans);
    }
    return 0;
}
