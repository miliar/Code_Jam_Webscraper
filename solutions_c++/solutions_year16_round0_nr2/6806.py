#include<stdio.h>
#include<string.h>

char s[1000];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("large_output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for(int _t = 1; _t <= t; _t++)
    {
        scanf(" %s", s);

        int countdiff = 0;
        for(int i = 1; s[i] != '\0'; i++)
            if(s[i] != s[i-1]) countdiff++;

        printf("Case #%d: %d\n", _t, countdiff + ((s[strlen(s)-1] == '-')? 1:0));
    }
}
