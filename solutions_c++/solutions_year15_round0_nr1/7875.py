#include <cstdio>

const int k_maxDataSize = 1010;
char data[k_maxDataSize];

int main()
{
    int T = 0;

    scanf("%d", &T);

    for(int i = 0; i < T; ++i) {
        int maxS = 0;

        scanf("%d", &maxS);

        scanf("%s", data);

        int addedNew = 0;
        int sum = 0;

        for(int j = 0; j < maxS + 1; ++j) {
            if(sum >= j)
                sum += data[j] - '0';
            else {
                addedNew += j - sum;
                sum += j - sum + data[j] - '0';
            }
        }

        printf("Case #%d: %d\n", i + 1, addedNew);
    }
}
