#include <iostream>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; ++test)
    {
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);

        printf("Case #%d:", test);

        for (int i = 1; i <= S; ++i)
            printf(" %d", i);

        printf("\n");
    }

    return 0;
}
