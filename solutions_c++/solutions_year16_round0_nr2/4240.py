#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char str[110];

void rev(int to)
{
    for(int i = 0; i <= to; ++i)
    {
        if(str[i] == '-')
        {
            str[i] = '+';
        }
        else
        {
            str[i] = '-';
        }
    }
}

int main()
{

	freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T, kase = 0;
    scanf("%d",&T);
    while(T--)
    {
        int ans = 0;
        scanf("%s", str);
        for(int i = strlen(str); i >= 0; --i)
        {
            if(str[i] == '-')
            {
                ++ans;
                rev(i);
            }
        }
        printf("Case #%d: %d\n", ++kase, ans);
    }
    return 0;
}
