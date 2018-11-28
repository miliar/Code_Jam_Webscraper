#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <string.h>
#include <algorithm>

using namespace std;

int T, N, av[1001], bv[1001];
double a[1001], b[1001];
int go1() {
    memset(av, 0, sizeof(av));
    memset(bv, 0, sizeof(bv));
    int score = 0;
    for(int i = 0; i < N; i++) {
        int index = -1;
        for(int j = 0; j < N; j++) if (!bv[j] && a[i] < b[j]) {
            index = j;
            break;
        }

        if (index == -1) {
            score++;        
            for(int j = 0; j < N; j++) if (!bv[j]) {
                bv[j] = 1;
                break;
            }
        } else {
            bv[index] = 1;
        }
    }

    return score;
}
int go2() {
    memset(av, 0, sizeof(av));
    memset(bv, 0, sizeof(bv));
    int p1 = 0, p2 = 0, score = 0;
    for(int i = 0; i < N; i++) {
        if (a[p1] > b[p2]) {
            score++;
            p1++;p2++;
        } else {
            p1++;
        }
    }

    return score;
}
int main() {
    freopen("war.in","r",stdin);
    freopen("war.out","w",stdout);
    cin >> T;
    int caseNumber = 1;
    while(T-- > 0) {
        cin >> N;
        for(int i = 0; i < N; i++) cin >> a[i];
        for(int i = 0; i < N; i++) cin >> b[i];
        sort(a, a + N);
        sort(b, b + N);

        printf("Case #%d: %d %d\n", caseNumber++, go2(), go1());
    }
    return 0;
}
