#include <bits/stdc++.h>
using namespace std;

const int MAX = 220;
double p[MAX];
int chosen[MAX], votes[MAX];
bool voteyes[MAX];
int n, k;
double best, sum;

void p2() {
    double prob = 1;
    for (int i = 0; i < k; i++) {
        prob *= p[chosen[votes[i]]];
    }
}

void p1() {
    for (int i = 0; i < n; i++) {
        //choose(k - 1, k / 2);
    }
}

void vote(int most, int left) {
    if (left == 0) {
        memset(voteyes, 0, sizeof(voteyes));
        for (int i = 0; i < k / 2; i++)
            voteyes[votes[i]] = true;
        double yes = 1, no = 1;
        for (int i = 0; i < k; i++) {
#ifdef DEBUG
            printf("%d%c ", chosen[i], voteyes[i] ? 'Y' : 'N');
#endif
            if (voteyes[i])
                yes *= p[chosen[i]];
            else
                no *= 1 - p[chosen[i]];
        }
#ifdef DEBUG
        printf(" p = %.3lf %.3lf %.3lf\n", yes, no, yes * no);
#endif
        sum += yes * no;
        return;
    }
    for (int i = most; i >= left - 1; i--) {
        votes[left - 1] = i;
        vote(i - 1, left - 1);
    }
}

void choose(int most, int left) {
    if (left == 0) {
#ifdef DEBUG
        for (int i = 0; i < k; i++)
            printf("%d ", chosen[i]);
        puts("");
#endif
        sum = 0;
        vote(k - 1, k / 2);
        if (best < sum)
            best = sum;
        return;
    }
    for (int i = most; i >= left - 1; i--) {
        chosen[left - 1] = i;
        choose(i - 1, left - 1);
    }
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; cs++) {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++)
            scanf("%lf", &p[i]);
        best = 0;
        choose(n - 1, k);
        printf("Case #%d: %.9lf\n", cs, best);
    }
}
