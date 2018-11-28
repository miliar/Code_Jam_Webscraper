#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <map>

#include "primes.h"

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

long
convert_base(const char *jambuf, int base)
{
    if (base == 10)
        return atol(jambuf);
    int len = strlen(jambuf);
    long num = 0;
    for (int l = len-1; l >= 0; l--)
        if (jambuf[l] != '0')
        {
            int b = len-1-l;
            if (b == 0)
                num++;
            else
            {
                long m = base;
                for (int i = 1; i < b; i++)
                    m *= base;
                num += m;
            }
        }
    return num;
}

long
get_first_divisor(long number)
{
    // start from 3 as 2 is not possible
    for (int i = 1; i < 10000; i++)
    {
        if (primes[i] >= number)
            break;
        
        if (number % primes[i] == 0)
            return primes[i];
    }
    return 0;
}

char *
btoa(char *buf, int len, int i)
{
    char *p = buf + len - 1;	/* points to terminating '\0' */
    // don't terminate
    //*p = '\0';
    if (i >= 0)
    {
        do {
            *--p = '0' + (i % 2);
            i /= 2;
        }
        while (i != 0);
        --p;
    }

    while (p >= buf)
    {
        *p = '0';
        p--;
    }

    return buf;
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

    for (int test_num = 0; test_num < num_tests; test_num++)
    {
        fgets(buf, 10001, f);
        int vals[10];
        get_cols(buf, vals);

        int N = vals[0];
        int J = vals[1];

        char jambuf[35];
        int factors[35];
        memset(jambuf, '0', N);
        jambuf[0] = '1';
        jambuf[N-1] = '1';
        jambuf[N] = '\0';

        int trynum = 0;

        printf("Case #%d:\n", test_num+1);
        for (int count = 0; count < J; count++)
        {
            btoa(jambuf+1, N-1, trynum);
            trynum++;
            
            // find a number.
            int found = 0;
            while (!found)
            {
                found = 1;
                for (int base = 2; base <= 10; base++)
                {
                    long number = convert_base(jambuf, base);
                    factors[base-2] = get_first_divisor(number);
                    if (factors[base-2] == 0)
                    {
                        found = 0;
                        break;
                    }
                }
                
                if (found == 0)
                {
                    btoa(jambuf+1, N-1, trynum);
                    trynum++;
                }
            }

            printf("%s", jambuf);
            for (int i = 2; i <= 10; i++)
                printf(" %d", factors[i-2]);
            printf("\n");
        }
    }

    fclose(f);

    return 0;
}

int
xmain(int argc, char **argv)
{
    for (int base = 2; base <= 10; base++)
    {
        long number = convert_base("1000000011100001", base);
        int divisor = get_first_divisor(number);
        printf("%ld %d\n", number, divisor);
    }
    return 0;
}

