#include <cstdio>
#include <cstring>

char pancakes[105];

inline void solve() {
    scanf("%s", pancakes);
    int count = strlen(pancakes);
    bool reversed = 0;
    int answer = 0;
    for(int i = count - 1; i >= 0; i--) {
        if (!reversed) {
            if (pancakes[i] == '-') {
                reversed = true;
                answer += 1;
            }
        } else {
            if (pancakes[i] == '+') {
                reversed = false;
                answer += 1;
            }
        }
    }
    printf("%d\n", answer);
}

int main() {
    int testcount;
    scanf("%d", &testcount);

    for(int test = 1; test <= testcount; test++) {
        printf("Case #%d: ", test);
        solve();
    }
}
