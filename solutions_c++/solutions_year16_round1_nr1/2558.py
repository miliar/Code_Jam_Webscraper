#include <stdio.h>
#include <string.h>
#include <deque>
#define MAXN 1005
using namespace std;

deque <int> dq;
char s[MAXN];

int main(void) {
    int t;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        dq = deque <int>();
        scanf(" %s", s);
        int n = strlen(s);

        for (int i = 0; i < n; i++) {
            int idx = s[i] - 'A';
            if (dq.empty()) {
                dq.push_front(idx);
            } else {
                if (dq.front() > idx) {
                    dq.push_back(idx);
                } else {
                    dq.push_front(idx);
                }
            }
        }
        printf("Case #%d: ", caso);
        while(!dq.empty()) {
            printf("%c", dq.front() + 'A');
            dq.pop_front();
        }
        printf("\n");
    }
    return 0;
}
