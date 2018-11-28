#include <bits\stdc++.h>
using namespace std;

long long min_ans;
char ans_a[100], ans_b[100];
char a[100], b[100];

void updateAns(char pa[], char pb[]) {
    long long ta = atoll(pa);
    long long tb = atoll(pb);
    if (min_ans > abs(ta - tb)) {
        min_ans = abs(ta - tb);
        strcpy(ans_a, pa);
        strcpy(ans_b, pb);
    }
    else if (min_ans == abs(ta - tb)) {
        int ret1 = strcmp(ans_a, pa);
        int ret2 = strcmp(ans_b, pb);
        if (ret1 > 0 || ret1 == 0 && ret2 > 0) {
            strcpy(ans_a, pa);
            strcpy(ans_b, pb);
        }
    }
}

void ToFill(int s, bool less) {
    int n = strlen(a);
    char tmp_a[100], tmp_b[100];
    strcpy(tmp_a, a);
    strcpy(tmp_b, b);
    if (less) {
        for (int i = s; i < n; i++)
            if (tmp_a[i] == '?')
                tmp_a[i] = '9';
        for (int i = 0; i < n; i++)
            if (tmp_b[i] == '?')
                tmp_b[i] = '0';
    }
    else {
        for (int i = s; i < n; i++)
            if (tmp_a[i] == '?')
                tmp_a[i] = '0';
        for (int i = 0; i < n; i++)
            if (tmp_b[i] == '?')
                tmp_b[i] = '9';
    }
    updateAns(tmp_a, tmp_b);
}

void DoFix(int s) {
    int n = strlen(a), i;
    for (i = s; i < n; i++) {
        if (a[i] == '?' && b[i] == '?') {
            a[i] = '0', b[i] = '1';
            ToFill(i, a[i] < b[i]);
            a[i] = '1', b[i] = '0';
            ToFill(i, a[i] < b[i]);
            a[i] = b[i] = '0';
        }
        else if (a[i] == '?') {
            int st = b[i] - 1 >= '0' ? b[i] - 1 : '0';
            int end = b[i] + 1 <= '9' ? b[i] + 1 : '9';
            for (int j = st; j <= end; j++) {
                a[i] = j;
                if (b[i] == j)
                    DoFix(i + 1);
                else
                    ToFill(i, a[i] < b[i]);
                a[i] = '?';
            }
            return;
        }
        else if (b[i] == '?') {
            int st = a[i] - 1 >= '0' ? a[i] - 1 : '0';
            int end = a[i] + 1 <= '9' ? a[i] + 1 : '9';
            for (int j = st; j <= end; j++) {
                b[i] = j;
                if (a[i] == j)
                    DoFix(i + 1);
                else
                    ToFill(i, a[i] < b[i]);
                b[i] = '?';
            }
            return;
        }
        else if(a[i] == b[i]) 
            continue;
        else {
            ToFill(i, a[i] < b[i]);
            return;
        }
    }
    updateAns(a, b);
}

int main() {
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, c = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%s %s", a, b);
        min_ans = 1e18;
        DoFix(0);
        printf("Case #%d: %s %s\n", c++, ans_a, ans_b);
    }
    return 0;
}