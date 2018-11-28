#include <stdio.h>

#include <algorithm>
using namespace std;

const int MX = 100;

int v[10];
void set(int n) {
    if (n==0)
        v[0] = 1;
    while (n>0) {
        v[n%10] = 1;
        n /= 10;
    }
}
int chk() {
    for (int i=0; i<10; i++)
        if (!v[i])
            return false;
    return true;
}
int calc(int n) {
    memset(v, 0, sizeof(v));
    for (int i=1; i<=MX; i++) {
        set(n*i);
        if (chk())
            return n*i;
    }
    return -1;
}


int main () {

    int n, t, res;
    scanf("%d", &t);
    for (int i=1; i<=t; i++) {
        scanf("%d", &n);
        res = calc(n);

        printf("Case #%d: ", i);
        if (res<0)
            printf("INSOMNIA");
        else
            printf("%d", res);
        puts("");
    }
    
}
