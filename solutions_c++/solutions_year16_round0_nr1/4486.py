#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <set>
using namespace std;

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        int x;
        scanf("%d", &x);
        long long last = x;
        set<int> seen;
        for (int i = 1; i < 1000000 && seen.size() < 10; ++ i) {
            last = (long long)i * x;
            long long cur = last;
            while (cur > 0) {
                int digit = cur % 10;
                cur /= 10;
                seen.insert(digit);
            }
        }
        if (seen.size() < 10) {
            printf("Case #%d: INSOMNIA\n", test);
        } else {
            printf("Case #%d: %d\n", test, last);
        }
    }
    return 0;
}
