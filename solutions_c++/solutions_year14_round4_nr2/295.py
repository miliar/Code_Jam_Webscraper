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
const int N = 1e3 + 7;
const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;



int n, a[N], b[N];
vector <int> A, B;
int Find(int x){
    for (int i = 0; i < n; i++) if (b[i] == x) return i;
}

int Go(int x, int y){
    int ret = 0;
    if (x < y) for (int i = x; i < y; i++) swap(b[i], b[i + 1]), ret++;
    else for (int i = x; i > y; i--) swap(b[i], b[i - 1]), ret++;
    return ret;
}

int main(){
    int CAS;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &CAS);
    for (int cas = 1; cas <= CAS; cas++){
        scanf("%d", &n);
        for (int i = 0; i < n; i++){
            scanf("%d", &a[i]);
            b[i] = a[i];
        }
        sort(a, a + n);
        int l = 0, r = n - 1, ans = 0;
        for (int i = 0; i < n; i++){
            int x = Find(a[i]);
            if (x - l < r - x){
                ans += Go(x, l);
                l++;
            }else ans += Go(x, r), r--;
        }

        printf("Case #%d: %d\n", cas, ans);
    }
}
