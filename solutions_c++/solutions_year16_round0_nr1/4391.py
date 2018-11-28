#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

void work() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        puts("INSOMNIA");
        return;
    }

    set<int> digits;
    for (int i = 0; i < 10; i++)
        digits.insert(i);

    int m = 0;
    while (!digits.empty()) {
        m += n;
        int x = m;
        while (x) {
            digits.erase(x % 10);
            x /= 10;
        }
    }

    printf("%d\n", m);
}

int main() {
    int T, C = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++C);
        work();
    }
}
