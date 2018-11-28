#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <cstring>
#include <stack>
#include <bitset>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int TS;
    int D, a, P[1111];
    scanf("%d",&TS);
    for (int ts = 1; ts <= TS; ts++) {
        priority_queue<int> Q;
        scanf("%d",&D);
        int maxx = 0;
        for (int i = 0; i < D; i++) {
            scanf("%d", &P[i]);
            maxx = max(maxx, P[i]);
        }
        int ans = 10000;
        for (int i = 1; i <= maxx; i++) {
            int temp = 0;
            for (int j = 0; j < D; j++) {
                int x = P[j] / i;
                if (P[j] % i == 0) x--;
                temp += x;
            }
            ans = min(ans, temp + i);
        }
        printf("Case #%d: %d\n",ts, ans);
    }
    return 0;
}
