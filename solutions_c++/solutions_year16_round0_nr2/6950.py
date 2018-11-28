#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char s[1000];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int oo;
    scanf("%d", &oo);
    for(int o = 0; o < oo; o++)
    {
        scanf("%s", &s);
        int len = strlen(s);
        int i = len - 1;
        while (i >= 0 && s[i] == '+')i--;
        int dhvan = 0;
        for(int j = i; j >= 0; j--)
            if (j + 1 == len || s[j] != s[j + 1])dhvan++;
        printf("Case #%d: %d\n", o + 1, dhvan);
    }
}
