#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=1100;
char s[maxn];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,ca=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        int n=strlen(s);
        int cur=1;
        char temp=s[0];
        for(int i=1;i<n;i++)
        {
            if(s[i]!=temp)
            {
                temp=s[i];
                cur++;
            }
        }
        if(temp=='+')
        cur--;
        printf("Case #%d: %d\n",ca++,cur);
    }
    return 0;
}
