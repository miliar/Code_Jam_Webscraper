#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int pancakes[1024];

void solve(int cnum) {
    memset(pancakes, 0, sizeof(pancakes));

    int d;
    scanf("%d", &d);

    int maxp = 0;

    for (int i = 0; i < d; ++i) {
        int curr;
        scanf("%d", &curr);
        ++pancakes[curr];
        if (curr > maxp) maxp = curr;
    }

    int result = 1<<30;

    for (int i = 1; i <= maxp; ++i) {
        // basically, try to go up to split pancakes into size up to maxp;
        int max_minutes = 0;
        int steps = 0;
        for (int j = 1; j <= maxp; ++j) {
            if (j <= i) {
                if (pancakes[j]) {
                    max_minutes = j;
                }
            } else {
                if (pancakes[j]) {
                    // split the pancakes into groups of size at most i
                    // if j is multiple of i do different calculation
                    if (j % i == 0) {
                        // j is multiple of i
                        // add enough steps to split into this
                        steps += pancakes[j] * ((j / i) - 1);
                    } else {
                        steps += pancakes[j] * (j / i);
                    }
                    max_minutes = i;
                }
            }
        }
        if (max_minutes + steps < result) {
            result = max_minutes + steps;
        }
        //printf("i %d res %d min %d st %d\n", i, result, max_minutes, steps);
    }

    printf("Case #%d: %d\n", cnum, result);
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}