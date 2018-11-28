#include <cstdio>
#include <cstdlib>
#include <cstring>

int T;
char cake[128], h;

int find_sad() {
    for (int i = h - 1; i >= 0; i--) {
        if (cake[i] == '-') {
            return i;
        }
    }
    return -1;
}

int happy() {
    return find_sad() == -1;
}

void flip() {
    for (int i = find_sad(); i >= 0; i--) {
        cake[i] = cake[i] == '+' ? '-' : '+';
    }
}

int solve() {
    int turn = 0;
    while (!happy()) {
        flip();
        turn++;
    }
    return turn;
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s", cake);
        h = strlen(cake);
        printf("Case #%d: %d\n", t, solve());
    }
}
