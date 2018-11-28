#include <bits/stdc++.h>
using namespace std;
int in[1001];
char s[1001];

int main()
{
//    freopen("B-large.in", "r", stdin);
//    freopen("out.txt", "w",    stdout);
    int t,qq=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        int len = strlen(s);
        int k = 0;
        for(int i=len-1;i>=0;i--) in[k++] = (s[i] == '+');
        bool bit = false;
        int ans = 0;
        int now ;
        for(int i=0;i<len;i++)
        {
            now = in[i] ^ bit;
            if(!now)
            {
                ans++;
                bit ^= 1;
            }
        }
        printf("Case #%d: %d\n",qq++,ans);
    }
    return 0;
}
