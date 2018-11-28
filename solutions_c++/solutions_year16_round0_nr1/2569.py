#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>

using namespace std;

int n;

void add_digits(long long number, set<int> *s)
{
    while (number != 0) {
        int res = number % 10;
        s->insert(res);
        number -= res;
        number /= 10;
    }
}

int main()
{
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i) {
        int x;
        scanf("%d", &x);

        set<int> S; int j;
        for (j = 1; j <= 1000000; ++j) {
            add_digits((long long)j * (long long)x, &S);

            if (S.size() == 10)
                break;
        }

        printf("Case #%d: ", i);
        if (S.size() == 10) {
            printf("%lld\n", (long long)j * (long long)x);
        } else {
            printf("INSOMNIA\n");
        }
    }
    return 0;
}
