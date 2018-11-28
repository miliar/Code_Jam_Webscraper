/**************************************************
 *        Problem:  Google Code Jam 2015 Qualification Round Problem C
 *         Author:  clavichord93
 *          State:  
 **************************************************/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int MAX_N = 10005;

const int nextState[4][4] = {{0, 1, 2, 3}, {1, 0, 3, 2}, {2, 3, 0, 1}, {3, 2, 1, 0}};
const int nextSign[4][4] = {{0, 0, 0, 0}, {0, 1, 0, 1}, {0, 1, 1, 0}, {0, 0, 1, 1}};

char s[MAX_N];
int state[MAX_N];
bool f[MAX_N][3][4][2];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int l, x;
        scanf("%d %d", &l, &x);
        int n = l * x;
        scanf("%s", s);
        for (int i = 1; i < x; i++) {
            for (int j = 0; j < l; j++) {
                s[i * l + j] = s[j];
            }
        }

        for (int i = 0; i < n; i++) {
            switch (s[i]) {
                case '1':
                    state[i] = 0;
                    break;
                case 'i':
                    state[i] = 1;
                    break;
                case 'j':
                    state[i] = 2;
                    break;
                case 'k':
                    state[i] = 3;
                    break;
            }
        }

        //for (int i = 0; i < n; i++) {
            //printf("%d ", state[i]);
        //}
        //printf("\n");

        memset(f, 0, sizeof(f));
        f[0][0][0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 4; k++) {
                    for (int l = 0; l < 2; l++) {
                        if (f[i][j][k][l]) {
                            {
                                int nk = nextState[k][state[i]];
                                int nl = l ^ nextSign[k][state[i]];
                                f[i + 1][j][nk][nl] = 1;
                                //printf("f[%d][%d][%d][%d] -> f[%d][%d][%d][%d]\n", i, j, k, l, i + 1, j, nk, nl);
                            }
                            if (k - j == 1 && j < 2 && l == 0) {
                                int nk = state[i];
                                f[i + 1][j + 1][nk][0] = 1;
                                //printf("f[%d][%d][%d][%d] -> f[%d][%d][%d][%d]\n", i, j, k, l, i + 1, j + 1, nk, 0);
                            }
                        }
                    }
                }
            }
        }

        bool ans = f[n][2][3][0];

        if (ans) {
            printf("Case #%d: YES\n", cas);
        }
        else {
            printf("Case #%d: NO\n", cas);
        }
    }

    return 0;
}

/*
const int main_stack = 16;
char my_stack[128<<20];

int main() {
    __asm__("movl %%esp, (%%eax);\n"::"a"(my_stack):"memory");
    __asm__("movl %%eax, %%esp;\n"::"a"(my_stack + sizeof(my_stack) - main_stack):"%esp");
    Main();
    __asm__("movl (%%eax), %%esp;\n"::"a"(my_stack):"%esp");
    return 0;
}
*/
