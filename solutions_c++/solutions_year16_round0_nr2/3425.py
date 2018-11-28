#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    char str[1000];
    char ab[1000];
    int t;
    scanf("%d",&t);
    for (int tt=1; tt<=t; tt++)
    {
        scanf("%s",str);
        printf("Case #%d: ",tt);
        ab[0] = str[0];
        int top = 1, len = strlen(str);
        for (int j=1; j<len; j++)
            if (str[j] != str[j-1])
                ab[top++] = str[j];
        ab[top] = '\0';
        if (ab[top-1] == '+')
            printf("%d\n",top-1);
        else
            printf("%d\n",top);
    }
    return 0;
}
