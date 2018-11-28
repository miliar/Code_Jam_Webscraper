#include <iostream>
#include <cstdio>
using namespace std;

void Solve(int no) {
    int maxlevel;
    scanf("%d ", &maxlevel);
    int sum = 0;
    int ans = 0;
    int shy;
    char ch;
    for (int i=0; i<=maxlevel; i++) {
        scanf("%c", &ch);
        shy = ch - '0';
        if (shy > 0) {
            if (i > sum) {
                ans += (i - sum);
                sum = i;
            } 
            sum += shy;
        }
    }
    printf("Case #%d: %d\n", no, ans);
}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int i=0; i<T; i++) {
        Solve(i+1);
    }
    return 0;
}