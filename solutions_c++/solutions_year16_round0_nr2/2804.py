#pragma warning(disable:4996)

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char s[104];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t,tt=0;
    scanf("%d", &t);
    while(t--) {
        scanf("%s", s);
        int n = strlen(s);

        int ans=0;
        for (int i=0; i<n-1; i++)
            if (s[i] != s[i+1])
                ans++;
        if (s[n-1] == '-') ans++;

        printf("Case #%d: %d\n", ++tt, ans);
    }

    return 0;
}
