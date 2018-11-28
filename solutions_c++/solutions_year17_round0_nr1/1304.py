#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
char str[1010];
int str_int[1010];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cnt, k;
    scanf("%d", &cnt);
    for(int c = 1; c <= cnt; ++c)
    {
        scanf("%s %d", str, &k);
        int rst = 0;
        int len = strlen(str);
        bool flag = 1;
        for(int i = 0; i < len; ++i)
            str_int[i] = str[i] == '+' ? 1 : 0;
        for(int i = 0; i + k <= len; ++i)
        {
            if(str_int[i]) continue;
            for(int j = 0; j < k; ++j)
                str_int[i + j] ^= 1;
            ++rst;
        }
        printf("Case #%d: ", c);
        for(int i = len - k; i < len; ++i)
            if(!str_int[i]) flag = 0;
        if(flag) printf("%d\n", rst);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
