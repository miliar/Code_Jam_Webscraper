#include <cstdio>

using namespace std;
int n, x, y;
int needs[1010];
int cc[1010][1010];
double answer;

void pre() {
    for (int i = 1; i <=1000; i++) {
        needs[i - 1] = i * (i * 2 - 1);
    }
    cc[1][0] = 1;
    cc[1][1] = 1;
    for (int i = 2; i <= 1000; i++) {
        cc[i][0] = 1;
        for (int j = 1; j < i; j++) {
            cc[i][j] = cc[i - 1][j - 1] + cc[i - 1][j];
        }
        cc[i][i] = 1;
    }
}

double calc(int l, int r, int h) { //level, remain, height
    if (r >= l * 2 - 1) {
        int right = r - (l * 2 - 2);
        if (right > h) return 1;
    }
    if (r <= h) return 0;
    if (x == 0) return 0;
    double result = 0;
    for (int i = 0; (i <= h) && (i <= r); i++) {
        result += cc[r][i];
    }
    for (int i = 0; i < r; i++) {
        result /= 2;
    }
    return 1 - result;
}

void work() {
    if (x < 0) x = -x;
    int level;
    for (int i = 0; i < 1000; i++) {
        if (needs[i] > n) {
            level = i - 1;
            n -= needs[i - 1];
            break;
        }
    }
    if ((x + y) / 2 <= level) {
        answer = 1;
        return;
    }
    if ((x + y) / 2 > level + 1) {
        answer = 0;
        return;
    }
    answer = calc(level + 2, n, y);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    pre();
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        scanf("%d%d%d", &n, &x, &y);
        work();
        printf("Case #%d: %g\n", tc, answer);
    }
    return 0;
}
