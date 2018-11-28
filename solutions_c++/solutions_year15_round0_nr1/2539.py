#include <cstdio>

#define ASCII 48

using namespace std;

void solve(int cnum) {
    int total = 0;
    int added = 0;

    int smax;
    scanf("%d", &smax);

    char str[1024];
    scanf("%s", str);

    for (int i = 0; i <= smax; ++i) {
        // get char
        int curr = ((int)str[i]) - ASCII;
        if (!curr) continue;
        if (total < i) {
            added += (i - total);
            total = i;
        }
        //printf ("\tit %d add %d tot %d\n", i, added, total);
        total += curr;
    }

    printf("Case #%d: %d\n", cnum, added);
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}