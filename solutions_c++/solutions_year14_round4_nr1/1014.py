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

const int N = 10010;
const int INF = 1000000000;
const long long Mod = 1000000007;


int n, m, a[N];
multiset<int> mp;
multiset<int>::iterator it;

void solve(){
    scanf("%d%d", &n, &m);
    mp.clear();
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
        mp.insert(a[i]);
    }
    sort(a, a+n);
    int ans = 0;
    for(int i=n-1; i>=0; i--){
        it = mp.lower_bound(a[i]);
        if(it==mp.end()||*it != a[i])
            continue;
        mp.erase(it);
        ans ++;
        it = mp.upper_bound(m-a[i]);
        if(it!=mp.begin()){
            it--;
            mp.erase(it);
        }
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("input10.txt", "r", stdin);
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
