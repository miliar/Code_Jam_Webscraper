#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string.h>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#define MAXN 1001
#define ll long long
#define INF 0x3f3f3f3f

using namespace std;

int t,n,v[10001];

int main(void){
    freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &t);

    for(int test = 1; test <= t; test++){
        scanf("%d", &n);
        scanf("%d", &v[0]);
        int first = 0, second = 0, last = 0, diff = 0;
        for(int i = 1; i < n; i++){
            scanf("%d", &v[i]);
            if(v[i] < v[i-1]){
                first += v[i-1] - v[i];
                diff = max(diff, v[i-1] - v[i]);
            }
        }
        for(int i = 1; i < n; i++){
            second += min(v[i-1], diff);
        }
        printf("Case #%d: %d %d\n", test, first, second);
    }
    return 0;
}
