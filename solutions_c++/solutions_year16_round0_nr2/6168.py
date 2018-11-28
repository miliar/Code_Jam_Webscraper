#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int N;
char pan[105];

int uncoordIdx(int bottom, int target) {
    for (int i=bottom; i>=0; --i)
        if (pan[i] != target)
            return i;
    return -1;
}

void printPanckaes() {
        printf(" > ");
        for (int i=0; i<N; ++i)
            printf("%c", pan[i] == 0? '-' : '+');
        printf("\n");

}

int flip(int top, int bottom, int target) {
    //printf("[[[[%d, %d, target=%d]]]\n", top, bottom, target);

    if (top >= bottom)
        return (pan[top] == target? 0 : 1);

    if (pan[top] == target)
        return flip(top, bottom, 1-target);
    else {
        for (int i=0; i<=bottom/2; ++i) {
            pan[i] = 1 - pan[i];
            pan[bottom-i] = 1 - pan[bottom-i];
            swap(pan[i], pan[bottom-i]);
        }
        if (bottom % 2 == 0)
            pan[bottom/2] = 1 - pan[bottom/2];

        //printPanckaes();

        int uncoord = uncoordIdx(bottom, target);
        //printf("  >> %d\n", uncoord);

        return flip(top, uncoord, target) + 1;
    }

}

int main() {

    int cases;
    scanf("%d\n", &cases);
    for(int test=1; test<=cases; ++test) {
        scanf("%s", pan);

        //printf(" > %s\n", pan);

        N = strlen(pan);
        for (int i=0; i<N; ++i)
            pan[i] = (pan[i] == '+'? 1 : 0);

        int uncoord = uncoordIdx(N-1, 1);
        int ans = flip(0, uncoord, 1);
        printf("Case #%d: %d\n", test, ans);
    }

    return 0;

}
