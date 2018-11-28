#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>


int isPalindrome(char a[])
{
    int length = 0, i, j;

    length = strlen(a);

    for(i = 0, j = length-1 ; i<length/2; i++, j--)
    {
        if(a[i]!=a[j])
        {
            return 0;
        }
    }
    //printf("%s\n", a);
    return 1;
}


int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    long long a = 0, b =0, i=0;
    int n, cnt;
    char str[50];

    //int ll = (int)sqrt(121.0);
    //sprintf(ar, "%d",  ll);

    while(scanf("%d", &n)!=EOF)
    {
        for(int k = 1 ; k<=n; k++)
        {
            a = 0;
            b = 0;
            i = 0;
            cnt = 0;

            scanf("%lld%lld", &a, &b);

            for(i = a; i<=b; i++)
            {
                //printf("%s\n", str);
                sprintf(str, "%lld",  i);
                if(isPalindrome(str))
                {
                    long double sq = 0;
                    sq = sqrt(i);
                    float f = fmod(sq, 1.0f);
                    if( f != 0.0f )
                    {
                        continue;
                    }
                    else
                    {
                        long long tp = (long long) sq;
                        sprintf(str, "%lld",  tp);
                        if(isPalindrome(str))
                        {
                            //printf("%s\n", str);
                            cnt++;
                        }
                    }
                }
            }
            printf("Case #%d: %d\n", k, cnt);
        }
    }
    return 0;
}
