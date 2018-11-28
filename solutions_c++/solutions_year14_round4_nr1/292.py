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
const int N = 1e4 + 7;
const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;

int a[N], v[N];


bool cmp(int a, int b){return a > b;}

int main(){
    int CAS, n, x;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++){
        scanf("%d%d", &n, &x);
        memset(v, 0, sizeof(v));
        for (int i = 1; i <= n; i++) scanf("%d", &a[i]);
        int ans = 0;
        sort(a + 1, a + n + 1, cmp);
        for (int i = 1; i <= n; i++)
        if (!v[i]){
            ans++;
            v[i] = 1;
            for (int j = i + 1; j <= n; j++)
            if (!v[j] && a[i] + a[j] <= x){
                v[j] = 1;
                break;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
