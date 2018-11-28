#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int is_palindrom(char* word)
{
    int a = 0,
        b = strlen(word) - 1;

    while(a <= b)
        if (word[a++] != word[b--])
            return 0;
    return 1;
}


 int main() {

    int t, a, b, i, many, num = 1;
    double ii;
    char buf[10];


    scanf("%d", &t);

    while(t--)
    {
        many = 0;
        scanf("%d %d", &a, &b);

        for (i = a; i <= b; i++)
        {
            itoa(i, buf, 10);

            if(is_palindrom(buf))
            {
                ii = sqrt((double)i);

                if (ii == floor(ii))
                {
                    itoa((int)ii, buf, 10);

                    if(is_palindrom(buf))
                    {
                        //printf("%d je palindrom\n", i);
                        many++;
                    }
                }
            }

        }

        printf("Case #%d: %d\n", num++, many);
    }

    return 0;
 }
