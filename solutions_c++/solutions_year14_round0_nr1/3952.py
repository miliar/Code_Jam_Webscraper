#include <cstdio>
using namespace std;

int main() {
    int t = 0, row = 0, first[4], second[4], trash = 0, result = 0;
    bool v = false, two_v = false;
    scanf("%d", &t);
    for (int ggg = 1; ggg <= t; ggg++) {
        v = false; two_v = false;
        scanf("%d", &row);
        for (int i = 1; i < 5; i++) {
            if (i == row) {
                for (int j = 0; j < 4; j++){
                    scanf("%d", &first[j]);
                }
            }
            else scanf("%d %d %d %d", &trash, &trash, &trash, &trash);
        }
        scanf("%d", &row);
        for (int i = 1; i < 5; i++) {
            if (i == row) {
                for (int j = 0; j < 4; j++) {
                    scanf("%d", &second[j]);
                }
                for (int g = 0; g < 4; g++) {
                for (int j = 0; j < 4; j++) {
                    if (second[j] == first[g]) {
                        if (!v) {
                            v = true;
                            result = second[j];
                        }
                        else {
                            two_v = true;
                        }
                    }
                }
                }
            }
            else scanf("%d %d %d %d", &trash, &trash, &trash, &trash);
        }
        if (!v) {
            printf("Case #%d: Volunteer cheated!\n", ggg);
        }
        else if (!two_v) {
            printf("Case #%d: %d\n", ggg, result);
        }
        else {
            printf("Case #%d: Bad magician!\n", ggg);
        }
    }
    return 0;
}
