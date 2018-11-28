#define debug if(0)
#include <string>
#include <iostream>
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
#define show(x) debug cout << #x << ": " << x << endl;

#define ALL(v) (v).begin(), (v).end()

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

LL B;
LL inf = (LL)1e15;

bool check(int k, LL win, const vector<LL>&xs, double &res){
    res = -1;
    LL inv = 0;
    LL inv2 = 0;
    REP(i,k){
        //if(xs[i]>win) return false;
        inv += win - xs[i];
    }
    for(int i=k; i<37; i++){
        if(xs[i] <= win){
            inv2 += win+1 - xs[i];
        }
    }
    if(inv+inv2>B) return false;
    res = 36 * double(inv)/double(k) - inv - inv2;
    REP(i,k){
        if(xs[i]>win) res = -1;
    }
    return true;
}

void solve(){
    vector<LL>XS(37,0);
    int n;
    scanf("%lld %d", &B, &n);
    REP(i,n) scanf("%lld", &XS[i]);
    sort(ALL(XS));

    double res = 0;
    for(int k=1; k<=37; k++){

        LL L = 0, R = 100000000000000000LL;
        while(L<=R){
            LL mid = (L+R)/2;
            double tmp;
            if(check(k, mid, XS, tmp)){
                L = mid+1;
            } else {
                R = mid-1;
            }
            res = max(res, tmp);
        } // */

        /*
        int best = 0;
        for(int win=0; win<=2100; win++){
            double tmp;
            check(k,win,XS,tmp);
            //printf("%d - %lf\n", win, tmp);
            if(tmp > res){
                res = tmp;
                best = win;
                printf("k %d, win %d\n",k,win);
            }
            res = max(res, tmp);
        } // */
    }
    printf("%.10lf\n", res);
}

int main(int argc,char *argv[]) {
    int T; scanf("%d", &T);
    for(int t=1; t<=T; t++){
        printf("Case #%d: ", t);
        debug cout << endl;
        solve();
    }
}
