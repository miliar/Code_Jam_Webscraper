#include <cstdio>
using namespace std;

int main(void) {
    FILE *pfile = fopen("A-large.in", "r");
    int T;
    char shyness[1001] = {0};
    fscanf(pfile, "%d", &T);
    for (int t = 1; t <= T; ++t) {
        int maxShyness;
        fscanf(pfile, "%d", &maxShyness);
        fscanf(pfile, "%s", shyness);
        int nfriends = 0;
        int prefixSum = shyness[0] - '0';
        for (int i = 1; i <= maxShyness; ++i) {
            if (prefixSum < i) {
                nfriends += i - prefixSum;
                prefixSum += i - prefixSum;
            }
            prefixSum += shyness[i] - '0';
        }
        printf("Case #%d: %d\n", t, nfriends);
    }
    return 0;
}
