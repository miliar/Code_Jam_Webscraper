#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

int compute_sol(char buffer[], int SMax) {
    vector<int> sum(SMax+1);
    for (int i = 0; i < SMax + 1; i++) {
        for (int k = 0; k <= i; k++) {
            sum[i] += buffer[k]; 
        }
    }
    int res = 0;
    for (int i = 0; i < SMax; i++) {
        if (res + sum[i] < i+1) {
            res += i+1 - (res+sum[i]);
            assert (res + sum[i] == 1+i);
        }
        assert(res + sum[i] >= i+1);
    }
    return res;
}

int main()  {
    int T;
    int SMax;
    char buffer[1002];

    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        scanf("%d", &SMax);
        scanf("%s", buffer);
        for (int j = 0; j <= SMax; j++) {
            buffer[j] = buffer[j] - '0';
        }
        int res = compute_sol(buffer, SMax); 
        printf("Case #%d: %d\n", i+1, res);
    }

    return 0;
}

 
