#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main () {
    vector <int> numbers;
    int t, n, cap;
    int point, end;
    int lesser, result;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases ++) {
        scanf("%d %d", &n, &cap);
        numbers.resize(n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &numbers[i]);
        }
        sort (numbers.begin(), numbers.end());
        point = 0;
        end = n - 1;
        result = 0;
        while ((point <= end) && (numbers [point] + numbers [end] <= cap)) point ++;
        point --;
        lesser = point;
        while (point < end) {
            result ++;
            if (numbers [point] + numbers [end] <= cap) point ++;
            else lesser --;
            end --;
        }
        if (point == end) {
            result ++;
            lesser --;
        }
        if (lesser > 0) result += (lesser + 1) / 2;

        printf("Case #%d: %d\n", cases, result);
    }
}
