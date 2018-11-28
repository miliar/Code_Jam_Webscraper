#include <cstdio>
#include <cstring>


using namespace std;


bool check(char *s, int n) {
    for (int i = 0; i < n; i++) {
        if (s[i] != '+') return false;
    }
    return true;
}

void turn(char *s, int n) {
    // puts(s);
    for (int i = 0; i < n-1; i++) {
        if (s[i] == '+') s[i] = '-';
        else s[i] = '+';

        if (s[i] == s[i+1]) return;
    }
}

int main() {
    int T;
    scanf("%d", &T);

    char s[1100];

    for (int i = 1; i <= T; i++) {
        scanf("%s", s);
        int n = strlen(s);
        s[n] = '+';
        n++;
        s[n] = 0;
        int ans = 0;

        while (!check(s, n)) {
            turn(s, n);
            ans++;
        }
        printf("Case #%d: %d\n", i, ans);
    }


    return 0;
}
