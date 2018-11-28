#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N = 100005;
int ca;
int n ;

void work() {
    scanf("%d", &n);
    if (n == 0) {
        puts("INSOMNIA");
        return;
    } 
    int mask = 0 , x = 0;    
    do {
        x += n;
        int y = x;
        while (y) {
            mask |= 1 << y % 10;
            y /= 10;
        }        
    } while (mask != 1023);
    printf("%d\n" , x);
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
