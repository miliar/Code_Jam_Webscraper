#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

const char flag[2] = {'-', '+'};
char str[125];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf(" %s", str);
        int i = 0, j = 1;
        while (str[j] != '\0')
        {
            if (str[i] != str[j])
            {
                i++;
                str[i] = str[j];
            }
            j++;
        }
        i++; //len
        if (str[0] == flag[i & 1]) i--;
        printf("Case #%d: %d\n", cas, i);
    }
    return 0;
}
