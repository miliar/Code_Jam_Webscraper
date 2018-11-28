#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

int D;
priority_queue<int> Q;
priority_queue<int> Q2;

void init() {
    D = -1;
    Q = priority_queue<int>();
}

void read_and_load() {
    int num;
    scanf("%d", &D);
    assert(Q.size() == 0);
    for(int i = 0; i < D; i++) {
        scanf("%d", &num);
        Q.push(num);
    }
    Q2 = priority_queue<int>(Q);
}

int get(double x) {
    if(x <= 3) {
        return 1;
    }
    return ceil(sqrt(x));
}

int solve() {

    int best = Q.top();
    int steps = 0;
    while(Q.top() != 1) {
        int top = Q.top();  Q.pop();

        best = min(best, steps + top);

        steps += 1;

        int x = get(top);

        //printf("%d %d\n", top, x);
        Q.push(x);
        Q.push(top - x);
    }
    best = min(best, steps + Q.top());
    return best;
}

int solve2() {

    int best = Q2.top();
    int steps = 0;
    while(Q2.top() != 1) {
        int top = Q2.top();  Q2.pop();

        best = min(best, steps + top);

        steps += 1;

        Q2.push(top / 2);
        Q2.push(top - top / 2);
    }
    best = min(best, steps + Q2.top());
    return best;
}

int main(int argc, char const *argv[]) {
    int cases;

    scanf("%d", &cases);
    for(int i = 1; i <= cases; i++) {
        init();
        read_and_load();
        printf("Case #%d: %d\n", i, min(solve(), solve2()));
    }
    return 0;
}