#include <stdio.h>
#include <stdlib.h>

using namespace std;

char NO[] = "NO";
char YES[] = "YES";

/*
'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}
'1':0
'i':1
'j':2
'k':3
'-1':4
'-i':5
'-j':6
'-k':7
*/

int table[8][8] = {
    {0, 1, 2, 3, 4, 5, 6, 7},
    {1, 4, 3, 6, 5, 0, 7, 2},
    {2, 7, 4, 1, 6, 3, 0, 5},
    {3, 2, 5, 4, 7, 6, 1, 0},
    {4, 5, 6, 7, 0, 1, 2, 3},
    {5, 0, 7, 2, 1, 4, 3, 6},
    {6, 3, 0, 5, 2, 7, 4, 1},
    {7, 6, 1, 0, 3, 2, 5, 4}
};

void tranform_input(char* input)
{
    while(*input) {
        *input = *input - 'i' + 1;
        ++input;
    }
}

const char* solve(int L, int X, char* s)
{
    int ri = 0;

    for(int xi = 0; xi < X; ++xi) {
        for(int i = 0; i < L; ++i) {
            ri = table[ri][s[i]];
            if(ri == 1) {
                int rj = 0;
                int j0 = i + 1;
                for(int xj = xi; xj < X; ++xj) {
                    for(int j = j0; j < L; ++j) {
                        rj = table[rj][s[j]];
                        if(rj == 2) {
                            int rk = 0;
                            int k0 = j + 1;
                            for(int xk = xj; xk < X; ++xk) {
                                for(int k = k0; k < L; ++k) {
                                    rk = table[rk][s[k]];
                                }
                                k0 = 0;
                            }
                            if(rk == 3) {
                                return YES;
                            }
                        }
                    }
                    j0 = 0;
                }
            }
        }
    }

    return NO;
}

const char* solve_case(void)
{
    int L, X;
    char *buf;

    scanf("%d %d\n", &L, &X);
    buf = (char*)malloc(L + 1);
    fgets(buf, L + 1, stdin);
    tranform_input(buf);

    return solve(L, X, buf);
}

int main(int argc, const char *argv[])
{
    int cases;

    scanf("%d\n", &cases);

    for(int c = 1; c <= cases; ++c) {
        printf("Case #%d: %s\n", c, solve_case());
    }

    return 0;
}
