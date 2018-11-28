#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int db; scanf("%d", &db);
    for (int i = 1; i<=db; i++) {
        int k,c,s; scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", i);
        for (int j = 1; j<=k; j++) printf(" %d", j);
        printf("\n");
    }
    return 0;
}
