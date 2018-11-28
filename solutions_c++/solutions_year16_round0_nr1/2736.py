#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <map>

void
get_cols(char *buf, int *vals)
{
    char *ptr = buf;
    char *p2;
    int c = 0;
    while ((p2 = strchr(ptr, ' ')) != NULL)
    {
        *p2 = '\0';
        int val = atoi(ptr);
        vals[c] = val;
        c++;
        ptr = p2+1;
    }

    int val = atoi(ptr);
    vals[c] = val;
}


int
main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf("Usage: %s <input.txt>\n", argv[0]);
        return 0;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f)
    {
        printf("Couldn't open file\n");
        return 0;
    }

    char buf[10001];
    fgets(buf, 10001, f);
    int num_tests = atoi(buf);

    //printf("Got %d tests\n", num_tests);
    char numbuf[1024];

    int comp = 0;
    for (int i = 1; i <= 10; i++)
        comp |= (1 << i);

    for (int test_num = 0; test_num < num_tests; test_num++)
    {
        fgets(buf, 10001, f);
        long answer1 = atoi(buf);

        if (answer1 == 0)
            strcpy(numbuf, "INSOMNIA");
        else
        {
            short bitmask = 0;
            long ans;
            for (long i = 0; i < 10000000; i++)
            {
                ans = (i+1) * answer1;
                snprintf(numbuf, 1024, "%ld", ans);
                for (int j = 0; numbuf[j] != '\0'; j++)
                {
                    int k = numbuf[j] - '0' + 1;
                    int b = 1 << k;
                    bitmask |= b;
                }
                if (bitmask == comp)
                    break;
            }
        }
        printf("Case #%d: %s\n", test_num+1, numbuf);
        //printf("Got %.0f - %.0f\n", lower, upper);
    }

    fclose(f);

    return 0;
}
