#include<iostream>
#include<cstdio>
#include<cstring>


using namespace std;



int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int ti = 1; ti <= T; ++ti) {
        printf("Case #%d: ", ti);

        int l, number;
        int count[16];
        memset(count, 0, sizeof(count));
        scanf("%d", &l);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &number);
                if (l == i + 1) {
                    count[number - 1]++;
                }
            }
        }
        scanf("%d", &l);
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                scanf("%d", &number);
                if (l == i + 1) {
                    count[number - 1]++;
                }
            }
        }
        int answer = -1;
        for (int i = 0; i < 16; ++i) {
            if (count[i] == 2) {
                if (answer == -1) {
                    answer = i + 1;
                } else {
                    answer = 0;
                }
            }
        }
        if (answer > 0) {
            printf("%d\n", answer);
        } else if (answer == 0) {
            printf("Bad magician!\n");
        } else {
            printf("Volunteer cheated!\n");
        }

    }

    return 0;

}
