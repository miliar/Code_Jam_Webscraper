#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

char s[110];

int main() {
    int T;
    scanf("%d",&T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ",t);
        scanf("%s",s);
        int len = strlen(s);
        int tot = 0;
        for (int i = 0; i < len; i++)
            if (i == 0 || s[i] != s[i - 1])
                tot++;
        if (s[0] == '+' && s[len - 1] == '+')
            printf("%d\n",tot - 1);
        if (s[0] == '+' && s[len - 1] == '-')
            printf("%d\n",tot);
        if (s[0] == '-' && s[len - 1] == '+')
            printf("%d\n",tot - 1);
        if (s[0] == '-' && s[len - 1] == '-')
            printf("%d\n",tot);
    }
    return 0;
}

