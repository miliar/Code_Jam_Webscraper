#include <bits/stdc++.h>

using namespace std;

#define N 10005
#define LL long long

int n;
LL m;
int Map[10][10];
char ss[N];
int pre[N];
int suf[N];

int valueof(char ch) {
    if (ch == 'i')
        return 2;
    else if (ch == 'j')
        return 3;
    else
        return 5;
}

void init() {
    Map[1][1] = 1;
    Map[1][2] = 2;
    Map[1][3] = 3;
    Map[1][5] = 5;
    Map[2][1] = 2;
    Map[2][2] = -1;
    Map[2][3] = 5;
    Map[2][5] = -3;
    Map[3][1] = 3;
    Map[3][2] = -5;
    Map[3][3] = -1;
    Map[3][5] = 2;
    Map[5][1] = 5;
    Map[5][2] = 3;
    Map[5][3] = -2;
    Map[5][5] = -1;
}

int mul(int a, int b) {
    if (a * b > 0) {
        return Map[labs(a)][labs(b)];
    }
    else {
        return -Map[labs(a)][labs(b)];
    }
}

int inv (int a) {
    if (labs(a) == 1)
        return a;
    else
        return -a;
}

int calc(int l, int r) {
    return mul(suf[l], inv(suf[r + 1]));
}

int find(int tar) {
    int tmp = 1;
    for (int i = 0; i < 4; i++) {
        if (tmp == tar)
            return i;
        tmp = mul(tmp, pre[n]);
    }

    return -1;
}

int main() {

    freopen("C-large.in", "r", stdin);
    freopen("c.out", "w", stdout);

    init();
    int test;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%d%lld", &n, &m);
        scanf("%s", ss + 1);
        pre[0] = 1;
        suf[n + 1] = 1;

        for (int i = 1; i <= n; i++) {
            pre[i] = mul(pre[i - 1], valueof(ss[i]));
        }

        for (int i = n; i >= 1; i--) {
            suf[i] = mul(valueof(ss[i]), suf[i + 1]);
        }

        printf("Case #%d: ", cas);

        if (n <= 1) {
            puts("NO");
            continue;
        }

        bool flag = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = i + 2; j <= n; j++) {
                if (calc(i + 1, j - 1) != 3) continue;
                if (pre[n] == 1) {
                    if (pre[i] == 2 && suf[j] == 5) {
                        flag = 1;
                        break;
                    }
                }
                else if (pre[n] == -1) {
                    if (labs(pre[i]) == 2 && labs(suf[j]) == 5) {
                        int cnt = 1;
                        if (pre[i] < 0) cnt++;
                        if (suf[j] < 0) cnt++;

                        if (cnt == 1 && m % 2 == 1) {
                            flag = 1;
                            break;
                        }
                        else if (cnt == 2 && m % 2 == 0 && m >= 2) {
                            flag = 1;
                            break;
                        }
                        else if (cnt == 3 && m >= 3 && m % 2 == 1) {
                            flag = 1;
                            break;
                        }
                    }
                }
                else {
                    int a = find(mul(2, inv(pre[i])));
                    int b = find(mul(inv(suf[j]), 5));

                    if (a != -1 && b != -1) {
                        if (m >= a + b && m % 4 == (a + b + 1) % 4) {
                            flag = 1;
                            break;
                        }
                    }
                }
            }

            if (flag) break;
        }

        if (flag) {
            puts("YES");
            continue;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = n; j >= 1; j--) {
                int tmp = mul(inv(suf[i + 1]), 3);
                tmp = mul(tmp, inv(pre[j - 1]));

                int ff = find(tmp);
                if (ff == -1) continue;

                if (pre[n] == 1) {
                    if (pre[i] == 2 && suf[j] == 5 && m >= 2) {
                            flag = 1;
                            break;
                    }
                }
                else if (pre[n] == -1) {
                    if (labs(pre[i]) == 2 && labs(suf[j]) == 5) {
                            int cnt = ff;
                            if (pre[i] < 0) cnt++;
                            if (suf[j] < 0) cnt++;

                            if (cnt == 0 && m % 2 == 0) {
                                flag = 1;
                                break;
                            }
                            else if (cnt == 1 && m % 2 == 1 && m >= 3) {
                                flag = 1;
                                break;
                            }
                            else if (cnt == 2 && m % 2 == 0 && m >= 4) {
                                flag = 1;
                                break;
                            }
                            else if (cnt == 3 && m >= 5 && m % 2 == 1) {
                                flag = 1;
                                break;
                            }
                    }
                }
                else {
                    int a = find(mul(2, inv(pre[i])));
                    int b = find(mul(inv(suf[j]), 5));
                    if (a != -1 && b != -1) {
                        if (m >= a + b + ff + 2 && m % 4 == (a + b + 2 + ff) % 4) {
                            flag = 1;
                            break;
                        }
                    }
                }
            }
            if (flag) break;
        }

        if (flag) {
            puts("YES");
            //continue;
        }
        else {
            puts("NO");
        }

    }
    return 0;
}
