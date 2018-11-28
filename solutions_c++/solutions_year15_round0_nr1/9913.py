#include <cstdio>
#include <string>

using namespace std;

int main() {
    int T, Smax;
    char shyness[1001];

    scanf("%d\n", &T);
    for (int C=1 ; C<=T ; C++) {
        scanf("%d ", &Smax);
        scanf("%s\n", shyness);

        //printf("%d ", Smax);
        //printf("%s\n", shyness);

        int peopleUp = shyness[0] - '0';
        int ans = 0;
        for (int k=1 ; k <= Smax ; k++) {
            if (k > peopleUp) {
                int peopleNeeded = k - peopleUp;
                ans += peopleNeeded;
                peopleUp += peopleNeeded;
            }
            peopleUp += shyness[k] - '0';
        }

        printf("Case #%d: %d\n", C, ans);
    }
}
