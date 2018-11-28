#include <cstdio>
#include <algorithm>
using namespace std;

float Naomi[1003], Ken[1003];

int main() {
    int t = 0, n = 0, War = 0, Deceit = 0, Kp = 0, Np = 0, Wkp = 0, Wnp = 0;
    scanf("%d", &t);
    for (int ggg = 1; ggg <= t; ggg++) {
        Deceit = 0;
        Np = 0;
        Kp = 0;
        scanf("%d", &n);
        War = n;
        for (int i = 0; i < n; i++) {
            scanf("%f", &Naomi[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%f", &Ken[i]);
        }
        sort(Naomi, Naomi + n);
        sort(Ken, Ken + n);
        Np = 0; Kp = 0;
        Wnp = 0; Wkp = 0;
        while (Np < n) {
            if (Naomi[Np] > Ken[Kp] && Np < n) {
                Deceit++;
                Kp++;
            }
            Np++;
            if (Ken[Wkp] > Naomi[Wnp]) {
                War--;
                Wnp++;
            }
            Wkp++;
        }
        printf("Case #%d: %d %d\n", ggg, Deceit, War);
    }
    return 0;
}
