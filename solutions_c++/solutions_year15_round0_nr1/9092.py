#include <cstdio>
#include <cstring>

using namespace std;

int mydebug = 0;

#define MAXN 1005
int shy_levels[MAXN];

int calc_ovation(int length) {
    int added = 0, avail = 0, index = 0;
    while (index < length) {
        avail += shy_levels[index];
        if (avail > 0)
            avail--;
        else
            added++;
        index++;
    }
    return added;
}


int main() {
    if (mydebug == 0) {
        freopen("/Users/dy/Documents/uni/puzzles/compete/compete/google2alarge.in", "r", stdin);
        freopen("/Users/dy/Documents/uni/puzzles/compete/compete/google2alarge.out", "w", stdout);
    } else if (mydebug >= 1) {
        freopen("/Users/dy/Documents/uni/puzzles/compete/compete/google2atest5", "r", stdin);
    }
    int ncases, length;
    char digit;
    
    
    scanf("%d", &ncases);
    for (int casenum = 1; casenum <= ncases; casenum++) {
        scanf("%d", &length);
        length++;
        memset(shy_levels, 0, sizeof(shy_levels));
        for (int i = 0; i < length; i++) {
            scanf(" %c", &digit);
            shy_levels[i] = digit - '0';
        }
        printf("Case #%d: %d\n", casenum, calc_ovation(length));
    }
    
    return 0;
}