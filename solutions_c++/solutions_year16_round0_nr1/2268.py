#include <iostream>
#include <cstring>
using namespace std;

int s[10];
int t, c, n, step;

void fill(int x) {
    int temp;
    while(x) {
        temp = x % 10;

        if (s[temp] == 0) {
            step++;
            s[temp] = 1;
        }

        x /= 10;
    }
}


int main() {
    scanf("%d", &t);
    c = 1;
    while (t--) {
        scanf("%d", &n);

        memset(s, 0, sizeof (s));
        step = 0;

        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", c++);
            continue;
        }

        fill(n);

        int m = n;
        while (step < 10) {
             m += n;
             fill(m);
        }

        printf("Case #%d: %d\n", c++, m);
    }
    return 0;
}
