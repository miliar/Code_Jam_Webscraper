#include <cstdio>
#include <cmath>
#include <set>
#include <algorithm>
using namespace std;

#define MAXN 1001

int a;
int b;
std::set<int> solutions;

inline bool is_palindrome(int number) {
    int n = number, r = 0, d;
    while (n > 0) {
        d = n % 10;
        r = r * 10 + d;
        n = n / 10;
    }
    return number == r;
}

void build() {
    int n;
    int last = (int)(sqrt(MAXN)) + 1;
    for (int i = 1; i <= last; i++) {
        n = i * i;
        if (is_palindrome(i) && is_palindrome(n)) {
            //printf("insert: %d -> %d\n", i, n);
            solutions.insert(n);
        }
    }
}

inline int solve() {
    std::set<int>::iterator start, last;
    start = solutions.lower_bound(a);
    last = solutions.upper_bound(b);


    if (start == solutions.end()) {
        //printf("none\n");
        return 0;
    } else if (last == solutions.end()) {
        //printf("%d - none\n", *start);
        return std::distance(start, last);
    } else {
        //printf("%d - %d\n", *start, *last);
        return std::distance(start, last);
    }
}

int main() {
    int T;
    build();
    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d %d\n", &a, &b);
        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}
