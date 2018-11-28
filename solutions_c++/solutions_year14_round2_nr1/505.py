#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define N 105
#define VIC vector<pair<int, char> >

void print(VIC &vic) {
    for (int i = 0; i < vic.size(); i++)
        printf("%d%c ", vic[i].first, vic[i].second);
    printf("\n");
}

VIC read() {
    char s[N];
    VIC result;
    scanf("%s", s);
    int n = strlen(s);
    char ch = s[0];
    int count = 1;
    for (int i = 1; i < n; i++) {
        if (s[i] == ch) {
            count++;
        } else {
            result.push_back(make_pair(count, ch));
            count = 1;
            ch = s[i];
        }
    }
    result.push_back(make_pair(count, ch));
    // print(result);
    return result;
}

bool judge(VIC &lh, VIC &rh) {
    if (lh.size() != rh.size())
        return false;
    for (int i = 0; i < lh.size(); i++) {
        if (lh[i].second != rh[i].second)
            return false;
    }
    return true;
}

int solve(vector< VIC > &strings) {
    int result = 0, n = strings.size(), m = strings[0].size();
    for (int i = 0; i < m; i++) {
        int *num = new int[n];
        memset(num, 0, sizeof(int) * n);
        for (int j = 0; j < n; j++)
            num[j] = strings[j][i].first;
        sort(num, num + n);
        int mid = 0;
        if (n % 2 == 0)
            mid = (num[n / 2] + num[n / 2 - 1]) >> 1;
        else
            mid = (num[n / 2]);
        for (int j = 0; j < n; j++)
            result += abs(mid - num[j]);
    }
    return result;
}

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, n;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        vector< VIC > strings;
        scanf("%d", &n);
        for (int j = 0; j < n; j++)
            strings.push_back(read());
        bool lost = false;
        for (int j = 1 ; j < n; j++) {
            if (!judge(strings[j], strings[j - 1])) {
                lost = true;
                break;
            }
        }
        if (lost)
            printf("Case #%d: Fegla Won\n", i);
        else
            printf("Case #%d: %d\n", i, solve(strings));
    }
    return 0;
}
