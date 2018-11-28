#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void
readLimits(char *buf, double *lower, double *upper)
{
    char *ptr = strchr(buf, ' ');
    *ptr = '\0';
    *lower = atoi(buf);
    *upper = atoi(ptr+1);
}

bool
isPalindrome(double v)
{
    char buf[1024];
    sprintf(buf, "%.0f", v);
    //printf("%s\n", buf);
    int len = strlen(buf);
    int l2 = (int)(len / 2);
    //printf("%d\n", l2);
    for (int i = 0; i < l2; i++)
    {
        if (buf[i] != buf[len-i-1])
        {
            //printf("%c != %c\n", buf[i], buf[len-i-1]);
            return false;
        }
    }

    return true;
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
        double lower;
        double upper;
        readLimits(buf, &lower, &upper);
        long numCases = 0;
        for (double x = lower; x <= upper; x += 1.0)
        {
            if (isPalindrome(x))
            {
                double x2 = (double)sqrt(x);
                double c;
                modf(x2, &c);
                double chk = c * c;
                if (x - chk == 0.0)
                {
                    if (isPalindrome(x2))
                    {
                        //printf("x2 = %f, chk = %f\n", x2, chk);
                        //printf("%.0f is a palindrome and %.0f is a palindrome\n", x, x2);
                        numCases++;
                    }
                }
            }
        }
        printf("Case #%d: %ld\n", test_num+1, numCases);
        //printf("Got %.0f - %.0f\n", lower, upper);
    }

    fclose(f);

    return 0;
}
