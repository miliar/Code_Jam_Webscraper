#include <cstdio>
#include <algorithm>
#include <cstring>
#include <list>

using namespace std;

char str[1020];
char tmp[1020];
char res[2040];

bool cmp(char a, char b) {
    return a > b;
}

int main() {
    int T;

    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase ++) {
        scanf("%s", str);
        /*
        int len = 0;
        while (str[len] != '\0') {
             tmp[len] = str[len];
             len ++;
        }
        tmp[len] = '\0';
        sort(tmp, tmp+len, cmp);
        */
        int left = 1010, right = 1010;
        str[right++] = str[0];
        for (int i = 1; str[i] != '\0'; i++) {
            if (str[i] >= str[left]) {
                 str[--left] = str[i];
            } else {
                str[right++] = str[i];
            }
        }
        str[right++] = '\0';
        printf("Case #%d: %s\n", kase, str+left);
    }

    return 0;
}
