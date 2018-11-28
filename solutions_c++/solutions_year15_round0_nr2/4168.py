#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#define min(a, b) (a) < (b) ? (a) : (b)
#define N 1002

using namespace std;

int solve(priority_queue<int> que) {
    if (que.empty()) {
        return 0;
    }

    int max_num = que.top();

    if (max_num <= 3) {
        return max_num;
    }

    que.pop();
    // 对最大数进行拆分
    int split_greater = (max_num + 1) / 2;
    int split_less = max_num - split_greater;

    if (max_num == 9) {
        priority_queue<int> que2(que);
        que2.push(3);
        que2.push(6);
        max_num = min(max_num, solve(que2) + 1);
    }

    que.push(split_greater);
    que.push(split_less);

    return min(max_num, solve(que) + 1);
}

int main() {
    int T, D;
    scanf("%d", &T);
    for (int cnt = 1; cnt <= T; ++cnt) {
        scanf("%d", &D);
        priority_queue<int> que;
        int tmp;
        for (int i = 0; i < D; ++i) {
            scanf("%d", &tmp);
            que.push(tmp);
        }

        printf("Case #%d: %d\n", cnt, solve(que));
    }

    return 0;
}