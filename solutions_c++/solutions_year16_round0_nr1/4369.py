#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

bool digits[16];
int seen;

bool processNum(int a) {
    while(a>0) {
        if (!digits[a%10]) {
            digits[a%10] = true;
            seen++;
        }
        a /= 10;
    }
    return seen == 10;
}

void setUp() {
    seen = 0;
    memset(digits, 0, sizeof(digits));
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, NT, n, i;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cin>>n;
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", T);
            continue;
        }
        setUp();
        for(i=1; ; ++i) {
            if (processNum(n*i)) break;
        }
        printf("Case #%d: %d\n", T, n*i);
    }
    return 0;
}
