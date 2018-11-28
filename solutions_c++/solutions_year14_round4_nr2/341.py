#pragma  comment(linker, "/STACK:36777216")
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define  lc(x) (x << 1)
#define  rc(x) (lc(x) + 1)
#define  lowbit(x) (x & (-x))
#define  PI    (acos(-1))
#define  lowbit(x) (x & (-x))
#define  EPS   1e-10
#define  MAXN  500055
#define  MAXM  2005
#define  LL    long long
#define  DB    double
#define  ULL   unsigned long long
#define  INF   0x7fffffff
#define  pb    push_back
#define  mp    make_pair
#define  MOD   1000000007

using namespace std;

int t, n, a[1005], cas;

vector <int> vec;

int main(){
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> t;
    while(t --){
        scanf("%d", &n);
        vec.clear();
        for(int i = 1; i <= n; i ++) scanf("%d", &a[i]), vec.pb(a[i]);
        sort(vec.begin(), vec.end());
        int ans = 0, l = 1, r = n;
        for(int i = 0; i < n; i ++){
            int pos;
            for(int j = 1; j <= n; j ++) if(a[j] == vec[i]) pos = j;
            //cout << vec[i] << ' ' << pos << endl;
            if(pos - l < r - pos){
                ans += (pos - l);
                for(int j = pos; j > l; j --) swap(a[j], a[j - 1]);
                l ++;
            }
            else{
                ans += (r - pos);
                for(int j = pos; j < r; j ++) swap(a[j], a[j + 1]);
                r --;
            }
        }
        printf("Case #%d: %d\n", ++ cas, ans);
    }
}
