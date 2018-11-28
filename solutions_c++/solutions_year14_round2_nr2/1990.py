#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <list>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
typedef long long ll;
#define FOR(i, b, e) for(int i = b; i < e; i++)
using namespace std;

int main()
{
    int T, A, B, K;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++) {
        int ans = 0;
        scanf("%d%d%d", &A, &B, &K);
        for (int i = 0; i < A; i++) {
            for (int j = 0; j < B; j++) {
                if ((i&j) < K) {
                    ans++;
                }
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
       
    return 0;
}
