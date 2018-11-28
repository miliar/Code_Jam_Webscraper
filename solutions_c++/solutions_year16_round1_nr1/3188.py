#include <cstdio>
#include <cstring>
#include <iostream>
#include "io.h"
using namespace std;


void toString(int n, char *str) {
    sprintf(str, "%d", n);
}

char str[2000];

int main() {
    setInput("a.in");
    setOutput("a.out");
    int T;
    int len;
    int n;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        char *pt = str;
        scanf("%s", str);
        string s = "";
        while ((*pt) != 0) {
            if (s.length() != 0) {
                if ((*pt) >= s[0]) {
                    s = (*pt)+s;
                } else {
                    s = s+(*pt);
                }
            } else {
                s = (*pt)+s;
            }
            pt++;
        }
        printf("Case #%d: ", t);
        cout << s << endl;
    }

    return 0;
}