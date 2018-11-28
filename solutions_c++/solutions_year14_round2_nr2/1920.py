#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testsCnt;
    scanf("%d", &testsCnt);
    for (int testN = 1; testN <= testsCnt; testN++) {
        int a, b, k;
        __int64 r = 0;
        scanf("%d%d%d", &a, &b, &k);
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ((i & j) < k)
                    r++;
            }
        }
        printf("Case #%d: %I64d\n", testN, r);
    }

}