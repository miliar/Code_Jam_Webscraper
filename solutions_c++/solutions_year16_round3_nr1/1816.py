#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T, P[26];

    cin >> T;

    for (t = 1; t <= T; ++t) {
        printf("Case #%d:", t);
        int N, total = 0, maxParty1, maxParty2, maxParty3;
        cin >> N;

        for (int i = 0; i < N; ++i) {
            cin >> P[i];
            total += P[i];
        }

        while (total) {
            maxParty1 = max_element(P, P + N) - P;
            P[maxParty1]--;
            total--;

            maxParty2 = max_element(P, P + N) - P;
            P[maxParty2]--;
            total--;

            if (total == 0) {
                printf(" %c%c", 'A' + maxParty1, 'A' + maxParty2);
                break;
            }

            maxParty3 = max_element(P, P + N) - P;

            if (P[maxParty3] > total / 2) {
                P[maxParty2]++;
                total++;
                printf(" %c", 'A' + maxParty1);
            }
            else {
                printf(" %c%c", 'A' + maxParty1, 'A' + maxParty2);
            }
        }

        puts("");
    }

    return 0;
}
