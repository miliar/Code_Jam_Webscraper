#include <cstdio>
#include <string.h>
using namespace std;
int main()
{
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; i++)
    {
        char s[1001];
        scanf("%s", s);
        int k;
        scanf("%d", &k);
        int count=0;
        bool flag=false;
        int u=strlen(s);
        for (int j=0; j<u; j++)
        {
            if ('-'==s[j])
            {
                if (j+k>u)
                {
                    flag=true;
                    break;
                }
                count++;
                for (int f=j; f<j+k; f++)
                {
                    if ('-'==s[f]) s[f]='+'; else s[f]='-';
                }
            }
        }
        printf("Case #%d: ", i+1);
        if (flag)
        {
            printf("IMPOSSIBLE");
        }
        else
        {
            printf("%d", count);
        }
        printf("\n");
    }
    return 0;
}
