/**************************************************
 *        Problem:  Google Code Jam 2015 Qualification Round Problem A
 *         Author:  clavichord93
 *          State:  
 **************************************************/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

const int MAX_N = 1005;

char s[MAX_N];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int smax;
        scanf("%d %s", &smax, s);
        int ans = 0;
        int sum = 0;
        for (int i = 0; i <= smax; i++) {
            int cnt = s[i] - '0';
            if (sum < i) {
                ans += i - sum;
                sum += i - sum;
            }
            sum += cnt;
        }
        printf("Case #%d: %d\n", cas, ans);
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
