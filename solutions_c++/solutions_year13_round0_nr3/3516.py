#include <cstdio>
#include <cmath>

using namespace std;

int T, A, B;

bool palin(int a) {
    int n[100], d=0;
    while (a > 0)
        n[d++] = a % 10, a /= 10;
    // printf("%d\n", d);
    for (int i=0 ; i<d/2 ; i++) {
        if (n[i] != n[d - i -1])
            return false;
    }

    return true;
}

int main() {
    scanf("%d", &T);
    for (int c=1 ; c<=T ; c++) {
        scanf("%d %d", &A, &B);
        int asdf = sqrt(A);
        int cnt = 0;
        for (int i=asdf ; i*i<=B ; i++) {
            if (i*i >= A && palin(i) && palin(i*i)) {
                cnt++;
            }
        }
        printf("Case #%d: %d\n", c, cnt);
    }
}