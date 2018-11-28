#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



//#define MY_DEBUG

#ifdef MY_DEBUG
    #define dout std::cout
    // See http://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
    #define dprintf(...) printf(__VA_ARGS__)
#else
    #define dout 0 && std::cout
    #define dprintf(...) 0 && printf(__VA_ARGS__)
#endif
//#define dprintf 0 && printf
    

#define STR_MAX_LEN 201
char S[STR_MAX_LEN + 1];


inline int FindFirstDifferent(char *S) {
    int i;
    int len = strlen(S);
    for (i = 1; i < len; i++) {
        if (S[i - 1] != S[i])
            return i;
    }
    return -1;
}

void DoIt(char *S) {
    int i, j;

    assert(strlen(S) > 0);

    dprintf("\n");
    for (i = 0; ; i++) {
        int pos = FindFirstDifferent(S);
        //assert(pos != -1);
        dprintf("pos = %d\n", pos);

        if (pos == -1) {
            // All chars in S are identical
            if (S[0] == '-') {
                dprintf("    Completely 'negating' S\n", S);
                printf("%d\n", i + 1);
            }
            else
            if (S[0] == '+')
                printf("%d\n", i);
            return;
        }

        // Change chars up to pos, exclusively
        for (j = 0; j < pos; j++) {
            if (S[j] == '-')
                S[j] = '+';
            else
            if (S[j] == '+')
                S[j] = '-';
        }

        dprintf("    S after 'negating' up to pos %03d exclusively = %s\n", pos, S);
    }
}

void Read() {
    int T;
    int val;

    //printf("Entered Read()\n");

    scanf("%d\n", &T);
    dprintf("T = %d\n", T);

    for (int idTest = 0; idTest < T; idTest++) {
        scanf("%s\n", S);
        dprintf("S = %s\n", S);

        printf("Case #%d: ", idTest + 1);
        DoIt(S);
    }
}

int main() {
    //freopen("A_small.in", "rt", stdin);
    //freopen("B-small-attempt0.in", "rt", stdin);
    freopen("B-large.in", "rt", stdin);

    Read();

    return 0;
}
