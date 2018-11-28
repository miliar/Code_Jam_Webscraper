#include <bits/stdc++.h>
using namespace std;
const int N = 100005;

int ca;
char str[N];

void work() {
    scanf("%s" , str);
    int res = 1 , n = strlen(str);
    for (int i = 1 ; i < n ; ++ i) {
        if (str[i] != str[i - 1])
            ++ res;
    }
    if (str[n - 1] == '+')
        -- res;
    printf("%d\n" , res);
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
