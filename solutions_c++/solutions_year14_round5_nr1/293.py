#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define MP make_pair

typedef double DB;
typedef long long LL;
typedef pair<int,int> PI;

const DB eps = 1e-6;
const int N = 1e6 + 7;
const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;



LL sum[N];


LL Calc(int R){
    int l = 1, r = R, t;
    while (l <= r){
        int mid = l + r >> 1;
        if (sum[R] - sum[mid] > sum[mid - 1]){
            t = mid;
            l = mid + 1;
        }else r = mid - 1;
    }
    LL ret = max(sum[R] - sum[t], sum[t]);
    if (t != R) ret = min(ret, max(sum[R] - sum[t + 1], sum[t + 1]));
    return ret;
}

int main(){
    int CAS;
    LL n, p, q, r, s;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    //printf("%d\n", CAS);
    for (int cas = 1; cas <= CAS; cas++){
        cin >> n >> p >> q >> r >> s;
        for (int i = 1; i <= n; i++){
            sum[i] = sum[i - 1] + ((i - 1) * p + q) % r + s;
        }
        LL ans = 0;
        for (int i = 0; i <= n; i++) ans = max(ans, min(sum[i], sum[n] - sum[i]));
        for (int i = 2; i < n; i++)
            ans = max(ans, sum[n] - max(sum[n] - sum[i], Calc(i)));
        printf("Case #%d: %.10lf\n", cas, (DB)ans / sum[n]);
    }
}
