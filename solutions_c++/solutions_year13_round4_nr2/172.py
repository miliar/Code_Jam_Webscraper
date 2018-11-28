#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cctype>
#include <queue>
#include <climits>
#include <sstream>
#include <cassert>
#include <iostream>
#include <cstdio>
#include <iostream>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR_EACH(it,v) for(__typeof((v).begin()) it = (v).begin(); it!=(v).end(); ++it)
#define show(x) cout << #x << ": " << x << endl;

template<typename T>
ostream& operator<<(ostream &o, const vector<T>&v){
    FOR_EACH(x, v){
        if(x==v.begin()) o << "[";
        else o << ", ";
        o << *x;
    }
    o << "]";
    return o;
}

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int>VI;
typedef vector<vector<int> >VII;

LL best_performance(LL t, LL n){
    LL w = (1LL<<n)-t-1; //worse
    LL b = (1LL<<n)-w-1;

    //printf("t %lld, w %lld, b %lld\n", t, w, b);

    LL res = 0;
    REP(i,n){
        res *= 2;
        if(w>0) {
            w--;
        } else {
            res++;
        }
        w = (w)/2;
        b = (b+1)/2;
    }
    //printf("best performance(%lld) = %lld\n", t, res);
    return res;
}

LL find_max_possible(LL n, LL p){
    LL L = 0, R = (1LL<<n) - 1, ans = 0;;
    while(L<=R){
        LL mid = (L+R)/2;
        if(best_performance(mid, n)<p){
            ans = mid;
            L = mid+1;
        } else {
            R = mid-1;
        }
    }
    return ans;
}

LL worst_performance(LL t, LL n){
    LL w = (1LL<<n)-t-1; //worse
    LL b = (1LL<<n)-w-1; //better

    LL res = 0;
    REP(i,n){
        res *= 2;
        if(b>0) {
            res++;
            b--;
            w = (w+1)/2;
            b = (b)/2;
        } else {
            w = (w+1)/2;
        }
    }
    return res;
}

LL find_min_guaranteed(LL n, LL p){
    LL L = 0, R = (1LL<<n) - 1, ans = 0;;
    while(L<=R){
        LL mid = (L+R)/2;
        if(worst_performance(mid, n)<p){
            ans = mid;
            L = mid+1;
        } else {
            R = mid-1;
        }
    }
    return ans;
}

void solve(){
    LL n,p;
    scanf("%lld %lld", &n, &p);
    LL a = find_min_guaranteed(n,p);
    LL b = find_max_possible(n,p);
    printf("%lld %lld", a,b);
    //exit(0);
}

int main(int argc,char *argv[]) {
    int T; scanf("%d", &T);
    for(int t=1; t<=T; t++){
        printf("Case #%d: ", t);
        solve();
        printf("\n");
    }
}
