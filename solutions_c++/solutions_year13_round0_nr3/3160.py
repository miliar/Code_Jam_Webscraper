/*
 * Author: tender
 * Created Time:  2013/4/13 20:28:41
 * File Name: c.cpp
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <set>

using namespace std;
const double pi = acos(-1.0);
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    int ans[] = {1, 4, 9, 121, 484};
    int cas;
    scanf("%d", &cas);
    for (int ii = 1; ii <= cas; ii++) {
        printf("Case #%d: ", ii);
        int a, b, res = 0;
        scanf("%d%d", &a, &b);
        for (int i = 0; i < 5; i++)
            if (ans[i] >= a && ans[i] <= b) res++;
        printf("%d\n", res);
    }
    return 0;
}
