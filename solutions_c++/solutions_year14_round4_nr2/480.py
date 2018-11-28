#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    int t, n;
    vector<int> numbers;
    int len, res;
    int mini, pos;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases ++) {
        scanf("%d", &n);
        numbers.resize(n);
        len = n;
        res = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &numbers [i]);
        }
        for (int i = 1; i < n; i++) {
            pos = -1;
            mini = 1000000009;
            for (int j = 0; j < len; j++) {
                if (numbers [j] < mini) {
                    mini = numbers [j];
                    pos = j;
                }
            }
            res += min (pos, len - pos - 1);
            for (int j = pos + 1; j < len; j++) {
                swap (numbers [j - 1], numbers [j]);
            }


            len --;
        }
        printf("Case #%d: %d\n", cases, res);
    }
}
