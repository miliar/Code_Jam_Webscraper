#include <stdio.h>
#include <stdlib.h>
#include <unordered_set>

int main()
{
    int t = 0;
    std::unordered_set<int> digits_seen;

    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        int n = 0;
        scanf("%d", &n);

        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", i + 1);
            continue;
        }

        int x = 1;
        digits_seen.clear();
        while (digits_seen.size() < 10) {
            int temp_n = n * x;
            while(temp_n > 0) {
                digits_seen.insert(temp_n % 10);
                temp_n /= 10;
            }
            ++x;
        }
        printf("Case #%d: %d\n", i + 1, n * (x - 1));
    }
    return 0;
}
