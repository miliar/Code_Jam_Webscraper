#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[5000];

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%s", s);
        int l = strlen(s);
        int ans = 0;
        for(int i = 0; i < l; ++i)
            if(i > 0 && s[i] != s[i - 1]) ++ans;
        if(s[l - 1] == '-') ++ans;
        printf("Case #%d: %d\n", Case, ans);
    }
    return 0;
}