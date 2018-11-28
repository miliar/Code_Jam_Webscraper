#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 1200

int n;
double Naomi[MAXN], Ken[MAXN];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas=1; cas<=T; ++cas) {
        scanf("%d", &n);
        for (int i=0; i<n; ++i)
            scanf("%lf", &Naomi[i]);
        for (int i=0; i<n; ++i)
            scanf("%lf", &Ken[i]);

        int huge, tiny;
        sort(Naomi, Naomi+n, less<double>());
        sort(Ken, Ken+n, less<double>());

        huge = 0;
        for (int i=0,j=0; i<n; ++i) {
            if (Naomi[i] > Ken[j]) {
                ++huge;
                ++j;
            }
        }

        sort(Naomi, Naomi+n, greater<double>());
        sort(Ken, Ken+n, greater<double>());

        tiny = 0;
        for (int i=0, j=0; i<n; ++i) {
            if (Ken[j] > Naomi[i]) {
                ++j;
            } else {
                ++tiny;
            }
        }

        printf("Case #%d: %d %d\n", cas, huge, tiny);
    }
    return 0;
}
