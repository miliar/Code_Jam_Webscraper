#include <cstdio>

using namespace std;

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int Smax;
        scanf("%d ", &Smax);

        int standing = 0, needed = 0, people;
        for (int i = 0; i <= Smax; i++) {
            people = (int)getchar() - '0';
            //printf("%d ", people);
            if (standing + needed < i) {
                needed = i - standing;
            }

            standing += (int)people;
        }

        printf("Case #%d: %d\n", t, needed);
    }

    return 0;
}