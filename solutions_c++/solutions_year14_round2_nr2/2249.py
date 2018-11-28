#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <utility>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;
unsigned long long int a, b, k, count1;

int main() {
    int cases = 1, t, i, j, sum, c, m, n, maximum, minimum;
    scanf("%d", &t);
    while (cases <= t) {
        count1 = 0;
        scanf("%llu %llu %llu", &a, &b, &k);
        for (i = 0; i < a; i++) {
            for (j = 0; j < b; j++) {
                c=i&j;
                if (((c) < k) && (c >= 0))        
                    count1++;
            }
        }
        printf("Case #%d: %llu\n", cases, count1);
        cases++;
    }
    return 0;
}

