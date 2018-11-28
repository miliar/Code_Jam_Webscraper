#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {

    int T, n, flips;
    char pancakes[201];

    scanf("%d\n", &T);

    for (int ts = 0; ts < T; ts++) {

        scanf("%s\n", pancakes);

        flips = 0;
        n = strlen(pancakes);
        for (int i = 1; i < n; i++) {
            if (pancakes[i] != pancakes[i-1])
                flips += 1;
        }
        if (pancakes[n-1] == '-')
            flips += 1;
        printf("Case #%d: %d\n", ts+1, flips);
    }
}
