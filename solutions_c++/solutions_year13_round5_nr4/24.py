#define debug if(0)
#include <cstring>
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

const int N = 20;
char buf[N+1];
int n;

double RES[1<<N];

double simulate(int &mask, int i){
    double res = n;
    while((mask & (1<<i))!=0){
        res--;
        i++;
        if(i==n) i = 0;
    }
    mask |= (1<<i);
    return res;
}

double go(int mask){
    if(mask == ((1<<n)-1)) return 0;
    double &res = RES[mask];
    if(res > 0.5) return res;
    res = 0;

    for(int i=0; i<n; i++){
        int m2 = mask;
        double tmp = simulate(m2, i);
        tmp += go(m2);
        res += tmp/n;
    }

    return res;
}

void solve(){
    scanf("%s", buf);
    n = strlen(buf);

    REP(m, (1<<n)){
        RES[m] = -1;
    }

    int mask = 0;
    REP(i,n){
        if(buf[i]=='X'){
            mask |= (1<<i);
        }
    }
    double RES = go(mask);
    printf("%.10lf\n", RES);
}

int main(int argc,char *argv[]) {
    int T; scanf("%d", &T);
    for(int t=1; t<=T; t++){
        printf("Case #%d: ", t);
        debug cout << endl;
        solve();
    }
}
