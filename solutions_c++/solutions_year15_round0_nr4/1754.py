/**************************************************
 *        Problem:  Google Code Jam 2015 Qualification Round Problem D Small
 *         Author:  clavichord93
 *          State:  
 **************************************************/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

bool ans[100][100][100];

int main() {
    ans[1][1][1] = 1;
    ans[1][1][2] = 0;
    ans[1][1][3] = 0;
    ans[1][1][4] = 0;

    ans[1][2][1] = 1;
    ans[1][2][2] = 1;
    ans[1][2][3] = 0;
    ans[1][2][4] = 0;

    ans[1][3][1] = 1;
    ans[1][3][2] = 0;
    ans[1][3][3] = 0;
    ans[1][3][4] = 0;

    ans[1][4][1] = 1;
    ans[1][4][2] = 1;
    ans[1][4][3] = 0;
    ans[1][4][4] = 0;

    ans[2][2][1] = 1;
    ans[2][2][2] = 1;
    ans[2][2][3] = 0;
    ans[2][2][4] = 0;

    ans[2][3][1] = 1;
    ans[2][3][2] = 1;
    ans[2][3][3] = 1;
    ans[2][3][4] = 0;

    ans[2][4][1] = 1;
    ans[2][4][2] = 1;
    ans[2][4][3] = 0;
    ans[2][4][4] = 0;

    ans[3][3][1] = 1;
    ans[3][3][2] = 0;
    ans[3][3][3] = 1;
    ans[3][3][4] = 0;

    ans[3][4][1] = 1;
    ans[3][4][2] = 1;
    ans[3][4][3] = 1;
    ans[3][4][4] = 1;

    ans[4][4][1] = 1;
    ans[4][4][2] = 1;
    ans[4][4][3] = 0;
    ans[4][4][4] = 1;

    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int x, r, c;
        scanf("%d %d %d", &x, &r, &c);
        if (r > c) {
            swap(r, c);
        }
        if (r * c % c && ans[r][c][x]) {
            cout << "hehe" << endl;
        }
        if (ans[r][c][x]) {
            printf("Case #%d: GABRIEL\n", cas);
        }
        else {
            printf("Case #%d: RICHARD\n", cas);
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
