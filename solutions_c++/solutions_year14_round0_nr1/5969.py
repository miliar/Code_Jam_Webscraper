#include <cstdio>
#include <set>

int main() {
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        std::set <int> set;
        for (int i = 1; i <= 16; ++ i) {
            set.insert(i);
        }
        for (int _ = 0; _ < 2; ++ _) {
            int row;
            scanf("%d", &row);
            for (int i = 1; i <= 4; ++ i) {
                for (int j = 1; j <= 4; ++ j) {
                    int a;
                    scanf("%d", &a);
                    if (i != row) {
                        set.erase(a);
                    }
                }
            }
        }
        printf("Case #%d: ", t);
        int size = set.size();
        if (size == 0) {
            puts("Volunteer cheated!");
        } else if (size == 1) {
            printf("%d\n", *set.begin());
        } else {
            puts("Bad magician!");
        }
    }
    return 0;
}
