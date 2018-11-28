#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

char s[1000100];

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    int T;
    scanf("%d", &T);

    int n;
    int i;
    int len;
    int cons;
    int val;
    int antes, depois;

    for (int I=1; I<=T; I++)
    {
        scanf("%s %d", s, &n);
        len = strlen(s);
        val = 0;
        cons = 0;
        antes = depois = 0;

        for (i=0; i<len; i++)
        {
            if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
                cons = 0;
            else
                cons++;

            if (cons==n) break;
        }
        //printf("cons=%d, n=%d, i=%d, antes=%d\n", cons, n, i, antes);
        antes = i-n+1;

        if (cons < n)
        {
            printf("Case #%d: 0\n", I);
            continue;
        }

        //printf("%d\n", val);

        for (i=i+1; i<len; i++)
        {
            if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
                cons = 0;
            else
                cons++;

            depois++;

            if (cons>=n)
            {
                depois--;
                val += (1+antes)*(1+depois);
                antes = i-n+1;
                //cons = 0;
                antes = i-n+1;
                depois = 0;
            }
        }

        //printf("%d\n", val);
        val += (1+antes)*(1+depois);

        printf("Case #%d: %d\n", I, val);

    }

    return(0);
}
