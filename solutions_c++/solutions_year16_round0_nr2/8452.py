#include <stdio.h>
#include <string.h>
#include <math.h>

int main (void)
{
    int t;
    scanf ("%d",&t);
    int i;
    for (i=0;i<t;++i)
    {
        int o=0;
        char s[100];
        scanf ("%s",s);
        int x=strlen(s);
        int p;
        if (x==1)
        {
            if (s[0]=='-')
                printf ("Case #%d: 1\n",i+1);
                else
                    printf ("Case #%d: 0\n",i+1);

        }
        else
            {
             for (p=0;p<x-1;++p)
            {
             if (s[p]!=s[p+1])
                o++;
            }

        if (s[x-1]=='+')
        {
            printf("Case #%d: %d\n",i+1,o);
        }
        else
            printf("Case #%d: %d\n",i+1,o+1);

    }
    }
    return 0;
}
