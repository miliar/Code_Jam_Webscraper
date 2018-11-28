#include <stdio.h>

using namespace std;

int main() {
    int t, smax, noOfPeople;
    freopen("A-large.in", "r", stdin);
    freopen("Answers", "w", stdout);

    scanf("%d", &t);
    for(int j = 1; j <= t; j++) {
        scanf("%d", &smax);

        int a[smax + 1];
        for(int i = 0; i <= smax; i++)
            scanf("%1d", &a[i]);

        int required = 0;
        noOfPeople = a[0];
        for(int i = 1; i <= smax; i++) {
            if(a[i] == 0) continue;
            if(noOfPeople < i) {
                required += (i - noOfPeople);
                noOfPeople = i;
            }
            noOfPeople += a[i];
        }
        printf("Case #%d: %d\n", j, required);
    }
    fclose(stdout);
    return 0;
}
