#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

#define PII pair<int,int> 
#define MP make_pair
#define FI first
#define SE second
#define PB push_back
#define LL(x) (x<<1)
#define RR(x) (x<<1|1)
#define MID(a,b) ((a+b)>>1)

const int N = 1010;
const int INF = 1000000000;
const long long Mod = 1000000007;


int n, m, a[N], vis[N], r[N];

bool cmpr(int i, int j){
    return a[i]<a[j];
}

void solve(){
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        scanf("%d", &a[i]);
        r[i] = i;
    }
    sort(r+1, r+n+1, cmpr);
    int ans = 0;
    for(int i=1; i<=n; i++){
        int p = r[i], l=0, rr=0;
        for(int j=1; j<p; j++){
            if(a[j]>a[p]){
                l++;
            }
        }
        for(int j=p+1; j<=n; j++){
            if(a[j]>a[p]){
                rr++;
            }
        }
        ans += min(l, rr);
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("input12.txt","r", stdin);
    freopen("output2.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        printf("Case #%d: ", i);
        solve();
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
