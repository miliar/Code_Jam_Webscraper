#include <bits/stdc++.h>
using namespace std;

char str[110];
char newchar(char c) {
    if (c == '-') {
        c = '+';
    }
    else {
        c = '-';
    }
    return c;
}

int main() {
    int t, icase = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%s", str);
        int len = strlen(str);
        int cnt = 0;
        printf("Case #%d: ", icase++);
        while (len >= 1) {
           while (len >= 1 && str[len - 1] == '+') {
               --len;
           }
           if (len < 1) {
               break;
           }
           bool flag = 0;
           for (int i = 0; i < len; ++i) {
               if (str[i] == '-') {
                   break;
               }
               str[i] = '-';
               flag = 1;
           }
           if (flag) {
               ++cnt;
           }
           for (int i = 0, j = len - 1; i <= j; ++i, --j) {
               if (i == j) {
                   str[i] = newchar(str[i]);
               }
               else {
                   char a = str[i], b = str[j];
                   str[i] = newchar(b);
                   str[j] = newchar(a);
               }
           }
           ++cnt;
        }
        printf("%d\n", cnt);
    }
    return 0;
}
