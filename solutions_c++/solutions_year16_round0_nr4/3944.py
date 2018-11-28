#include <bits/stdc++.h>

#define DEBUG 1

using namespace std;

#if DEBUG
    FILE* input = fopen("input.txt", "r");
    FILE* output = fopen("output.txt", "w");
    #define scanf(...) fscanf(input, __VA_ARGS__)
    #define printf(...) fprintf(output, __VA_ARGS__)
#endif // DEBUG

typedef long long int ll;

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int originalLen, generations, students;
        scanf("%d %d %d", &originalLen, &generations, &students);

        ll len = pow(originalLen, generations);
        ll diff = pow(originalLen, generations - 1);

        vector<ll> positions;

        /*ll curPosition = 1;
        for (int i = 0; i < students; i++) {
            if (curPosition < len && generations > 1) {
                curPosition++;
            }
            positions.push_back(curPosition);
            curPosition += (generations == 1 ? 1 : diff*2);

            if (curPosition > len) {
                break;
            }
        } */

        if (/*curPosition <= len */ false) {
            //printf("Case #%d: IMPOSSIBLE\n", t);
        } else {
            printf("Case #%d:", t);
            /*for (ll p : positions) {
                printf(" %lld", p);
            } */

            for (int i = 1; i <= students; i++) {
                printf(" %d", i);
            }
            printf("\n");
        }
    }
    return 0;
}
