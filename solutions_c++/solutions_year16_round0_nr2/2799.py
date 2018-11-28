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

void
trimchar(char *buf, char ch)
{
    for (int i = 0; buf[i] != '\0'; i++)
        if (buf[i] == ch)
        {
            buf[i] = '\0';
            break;
        }
}

void
invert(char *buf, int len)
{
    for (int i = 0; i <= len; i++)
        buf[i] = (buf[i] == '-' ? '+' : '-');
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

    for (int test_num = 0; test_num < num_tests; test_num++)
    {
        fgets(buf, 10001, f);
        trimchar(buf, '\n');

        int len = strlen(buf)-1;

        long attempt = 0;
        while (attempt < 100000)
        {
            int pivot;
            for (pivot = len; pivot >= 0; pivot--)
                if (buf[pivot] == '-')
                    break;
            if (pivot >= 0)
            {
                attempt++;
                invert(buf, pivot);
            }
            else
                break;
        }

        printf("Case #%d: %ld\n", test_num+1, attempt);
    }

    fclose(f);

    return 0;
}
