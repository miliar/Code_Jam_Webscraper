#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
            int K,C,S;
            scanf("%d %d %d", &K, &C, &S);
            printf("Case #%d: ", t+1);
            for (int i = 0; i < S-1; i++)
                printf("%d ", i+1);
            printf("%d\n", S);
    }
    return 0;
}
