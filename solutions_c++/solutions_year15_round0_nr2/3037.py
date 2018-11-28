#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define MP make_pair

typedef long double DB;
typedef long long LL;
typedef pair <int, int> PI;

const DB eps = 1e-8;
const int N = 2e5 + 7;
const int INF = 1e9 + 7;
const int MOD = 1e9 + 7;



int CAS, n;
int a[N];


int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++){
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        int ans = 1e9 + 7;
        for (int i = 1; i <= 1000; i++){
            int s = 0;
            for (int j = 0; j < n; j++)
                s += (a[j] - 1) / i;
            ans = min(ans, s + i);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}
