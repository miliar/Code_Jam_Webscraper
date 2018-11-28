#include <bits/stdc++.h>
using namespace std;
const int N = 105;

int ca;
int n , L;
string s[N] , B;
void work() {
    cin >> n >> L;
    for (int i = 0 ; i < n ; ++ i) {
        cin >> s[i];
    }
    cin >> B;
    for (int i = 0 ; i < n ; ++ i) {
        if (s[i] == B) {
            puts("IMPOSSIBLE");
            return;
        }
    }
    if (L > 1) {
        for (int i = 0 ; i < L + L ; ++ i) {
            putchar("0?"[i & 1]);
        } putchar(' ');
        for (int i = 0 ; i < L - 1 ; ++ i) {
            putchar('1');
        } puts("");
    } else {
        puts("0 ?");
    }

}

int main() {
    int T;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
