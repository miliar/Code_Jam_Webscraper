
#include <stdio.h>
#include <set>
#include <string.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

bool ispalin(int i)
{
    char s[100];
    s[0] = '\0';
    sprintf(s, "%d", i);

    int len = strlen(s);
    for (i = 0; i < len/2; ++i) {
        if (s[i] != s[len - i - 1])
            return false;
    }
    return true;
}

int fs(int l, int r)
{
    int count = 0;

    for (int i = l; i <= r; ++i) {
        if (ispalin(i)) {
            double sq = sqrt(i);
            if ((int)floor(sq) == (int)ceil(sq)) {
                if (ispalin((int)floor(sq))) {
                    ++count;
                }
            }
        }
    }

    return count;
}

int main(int argc, char **argv)
{
    int num_tests = 0;

    scanf("%d", &num_tests);

    for (int i = 0; i < num_tests; ++i) {
        int l, r;
        scanf("%d %d", &l, &r);
        printf("Case #%d: %d\n", i+1, fs(l, r));
    }

    return 0;
}


