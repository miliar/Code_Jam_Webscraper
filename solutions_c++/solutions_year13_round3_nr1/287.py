#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <memory.h>

using namespace std;

const int MAXN = 1000010;

char name[MAXN];
int consec[MAXN];
int n, len;

bool isConsonant(char letter) {
    return letter != 'a' && letter != 'o' &&
        letter != 'e' && letter != 'i' &&
        letter != 'u';
}

long long solve() {
    memset(name, 0, sizeof(name));
    memset(consec, 0, sizeof(consec));

    scanf("%s %d", &name, &n);
    len = strlen(name);

    if (isConsonant(name[0])) {
        consec[0] = 1;
    }

    long long res = 0;
    int maxStartPos = -1;

    if (consec[0] >= n) {
        maxStartPos = 0 - (n - 1);
    }

    if (maxStartPos != -1) {
        res += maxStartPos + 1;
    }

    for (int i = 1; i < len; i++) {
        if (isConsonant(name[i])) {
            consec[i] = consec[i - 1] + 1;
        } else {
            consec[i] = 0;
        }

        if (consec[i] >= n) {
            maxStartPos = i - (n - 1);
        }

        if (maxStartPos != -1) {
            res += maxStartPos + 1;
        }
    }

    return res;
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": " << solve() << endl;
    }

    return 0;
}
