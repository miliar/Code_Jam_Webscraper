
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    int caseNumber = 0;
    while (caseNumber < t) {
        caseNumber++;
        int shy;
        scanf("%d", &shy);
        char s[1011];
        scanf("%s", &s);
        int cnt = s[0] - '0';
        int add = 0;
        for (int i = 1; i <= shy; ++i) {
            if (cnt < i) {
                add += i - cnt;
                cnt = i;
            }
            cnt += s[i] - '0';
        }
        printf("Case #%d: %d\n", caseNumber, add);
    }
    return 0;
}
