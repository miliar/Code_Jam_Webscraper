#include <cstdio>

using namespace std;

int a, n;
int mote[110];
int f[110];

int answer;

void sort() {
    int tmp;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (mote[i] > mote[j]) {
                tmp = mote[i];
                mote[i] = mote[j];
                mote[j] = tmp;
            }
        }
    }
}

void work() {
    if ((a == 1) && (mote[0] >= 1)) {
        answer = n;
        return;
    }
    int curr = a;
    for (int i = 0; i < n; i++) {
        if (i == 0) f[i] = 0;
        else f[i] = f[i - 1];
        while(curr <= mote[i]) {
            curr += (curr - 1);
            f[i]++;
        }
        curr += mote[i];
    }
    answer = 1000000000;
    for (int i = 0; i < n; i++) {
        if (f[i] + n - i - 1 < answer) {
            answer = f[i] + n - i - 1;
        }
    }
    if (answer > n) answer = n;
}

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        scanf("%d%d", &a, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &mote[i]);
        }
        sort();
        work();
        printf("Case #%d: %d\n", tc, answer);
    }
    
    return 0;
}
