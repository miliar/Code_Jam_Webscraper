#include <cstdio>
#include <vector>

using namespace std;


int main() {
    int cases;
    scanf("%d", &cases);
    for (int c = 1; c <= cases; c++) {
        int d, max_cake = 0;
        vector<int> cakes;
        scanf("%d", &d);
        for(int i = 0; i < d; i++) {
            int t;
            scanf("%d", &t);
            cakes.push_back(t);
            if (max_cake < t)
                max_cake = t;
        }

        int ans = max_cake;
        for (int alloc = 2; alloc < ans; alloc++) {
            int sum = alloc;
            for (vector<int>::iterator it = cakes.begin(); it != cakes.end(); it++) {
                sum += (*it - 1) / alloc;
            }
            if (ans > sum)
                ans = sum;
        }

        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}
