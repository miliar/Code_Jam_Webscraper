#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int task = 1; task <= T; task++) {
        int s = 0, t = 0, p, num;
        cin >> p;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> num;
                if (i == p - 1) {
                    s |= 1 << num;
                }
            }
        }
        cin >> p;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> num;
                if (i == p - 1) {
                    t |= 1 << num;
                }
            }
        }
        if ((s & t) == 0) {
            printf("Case #%d: Volunteer cheated!\n", task);
        } else {
            int num = 0;
            for (int i = 1; i <= 16; i++) {
                if (s & t & (1 << i)) {
                    if (num) {
                        num = -1;
                        break;
                    }
                    num = i;
                }
            }
            if (num == -1) {
                printf("Case #%d: Bad magician!\n", task);
            } else {
                printf("Case #%d: %d\n", task, num);
            }
        }
    }
    
    return 0;
}
