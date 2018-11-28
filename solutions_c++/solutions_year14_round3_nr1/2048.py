
#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b) {
    if (a == b) return a;
    int max = (a > b) ? a : b;
    int min = (a < b) ? a : b;
    return gcd(max-min, min);
}

struct FRACTION {
    int n;
    int d;
};

FRACTION reduce(FRACTION f) {
    int d = gcd(f.n, f.d);
    FRACTION r;
    r.n = f.n/d; r.d = f.d/d;
    return r;
}

void push_over_half(FRACTION *f, int *count) {
    if ((f->n << 1) < f->d) {
        f->n = f->n << 1;
        *count = *count + 1;
        push_over_half(f, count);
    }
}

bool valid(FRACTION f) {
    return (f.d > 0) && !(f.d & (f.d-1)) && (f.n & 1);
}

int main(int argc, char * argv[]) {
    int cases;
    scanf("%d", &cases);
    for (int i=0; i<cases; ++i) {
        printf("Case #%d: ", i+1);
        FRACTION f;
        scanf("%d/%d", &f.n, &f.d); 
        FRACTION r = reduce(f);
        if (!valid(r)) { printf("impossible\n"); }
        else if (r.d == 1) { printf("0\n"); }
        else {
            int count = 0;
            push_over_half(&r, &count);
            printf("%d\n", count+1);
        }
    }
}
