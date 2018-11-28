#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#define zero(x) (((x)>0?(x):-(x))<eps)
//#include <bits/stdc++.h>
#define mem(a,b) memset((a),(b),sizeof((a)))
#define lld long long
#define INF 0x3f3f3f3f
#define eps 1e-6

using namespace std;

int n, m;
int num[100009];

int MAIN() {
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; i++) {
        scanf("%d", &num[i]);
    }
    sort(num, num + n);
    int sar = 0;
    int ans = 0;
    for(int i = n - 1; i >= sar; i--) {
        if(i == sar) {

            ans++;
            break;
        }
        if(num[i] + num[sar] <= m) {
            sar++;
        }
        ans++;
    }
    printf("%d\n", ans);
    return 0;
}

int main() {
#ifdef LOCAL_TEST
    freopen("F:/ACMData.txt","r",stdin);
    freopen("F:/out.txt","w",stdout);
#endif
    int cases;
    scanf("%d", &cases);
    int cc = 1;
    while(cases--) {
        printf("Case #%d: ", cc++);
        MAIN();
    }
    return 0;
}
