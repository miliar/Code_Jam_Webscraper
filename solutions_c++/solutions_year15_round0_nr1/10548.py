#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int sm;
char s[1100];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca = 1; ca <= t; ca++)
    {
        scanf("%d %s",&sm, s);
        int re = 0, pre = 0;
        int len = strlen(s);
        for(int i = 0; i < len; i++)
        {
            if(pre < i)
            {
                re += (i-pre);
                pre = i;
            }
            pre += (s[i]-'0');
        }
        for(int i = len; i <= sm; i++)
        {
            if(pre < i)
            {
                re += (i-pre);
                pre = i;
            }
        }
        printf("Case #%d: %d\n",ca,re);
    }
    return 0;
}
