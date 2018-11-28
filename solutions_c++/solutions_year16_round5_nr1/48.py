#include <bits/stdc++.h>
using namespace std;
const int N = 200005;

int ca;

int n;
char str[N];
int f[N][N];
void work() {
    scanf("%s" , str);
    n = strlen(str);
    stack< char > S;
    int res = n * 10;
    for (int i = 0 ; i < n ; ++ i) {
        if (S.empty() || S.top() != str[i]) {
            S.push(str[i]);
        } else {
            S.pop();
        }
    }
    res -= S.size() * 5;
    printf("%d\n" , res / 2);
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
