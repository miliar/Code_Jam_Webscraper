#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args)
#define foreach(_it,_v) for(typeof(_v.begin()) _it = _v.begin(); _it != _v.end(); ++_it)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const lint MOD = 1000002013;

class cmp {
public:
    bool operator()(pii a,pii b) {
        if(a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    }
};

vector<pii> vo,ve;
map<pii,lint> q;
int n,m;

bool by_e(pii a,pii b) {
    if(a.second != b.second) return a.second > b.second;
    return a.first < b.first;
}

lint cost(int o,int e,lint p) {
    lint d = e-o;
    return (p*d*n - p*(d*(d-1))/2) % MOD;
}

void erase(vector<pii> &v, pii p) {
    int i;
    for(i=0;i<v.size();++i) {
        if(v[i] == p) break;
    }
    swap(v[i],v[v.size()-1]);
    v.pop_back();
}

bool find(vector<pii> &v, pii p) {
    for(auto x: v) {
        if(x == p) return 1;
    }
    return 0;
}

int main() {
    int T;
    scanf("%d",&T);
    for(int _t = 1;_t <= T;++_t) {
        q.clear();
        vo.clear();
        ve.clear();
        printf("Case #%d: ",_t);
        scanf("%d%d",&n,&m);
        lint ans = 0;
        for(int a=0;a<m;++a) {
            int o,e,p;
            scanf("%d%d%d",&o,&e,&p);
            vo.push_back(pii(o,e));
            ve.push_back(pii(o,e));
            q[pii(o,e)] += p;
            ans += cost(o,e,p);
            ans %= MOD;
        }
        while(!ve.empty()) {
//            debug("size: %d\n",vo.size());
            sort(vo.begin(),vo.end());
            sort(ve.begin(),ve.end(),by_e);
//            debug("first e: (%d,%d)\n",ve[0].first,ve[0].second);
//            debug("first o: (%d,%d)\n",vo[0].first,vo[0].second);
            pii cur = ve[0];
            int i = 0;
            while(i < vo.size() && vo[i].second < cur.first) ++i;
            if(i >= vo.size() || vo[i].first >= cur.first) {
                erase(ve,cur);
                erase(vo,cur);
//                ans -= cost(cur.first,cur.second,q[cur]);
//                ans %= MOD;
                i += 1;
                continue;
            }
            pii cur2 = vo[i];
            int qmin = min(q[cur],q[cur2]);
            q[cur] -= qmin;
            q[cur2] -= qmin;
            pii new1 = pii(cur2.first,cur.second);
            pii new2 = pii(cur.first,cur2.second);
            q[new1] += qmin;
            q[new2] += qmin;
            if(!find(ve,new1)) ve.push_back(new1);
            if(!find(ve,new2)) ve.push_back(new2);
            if(!find(vo,new1)) vo.push_back(new1);
            if(!find(vo,new2)) vo.push_back(new2);
            if(q[cur] == 0) {
                erase(vo,cur);
                erase(ve,cur);
            }
            if(q[cur2] == 0) {
                erase(vo,cur2);
                erase(ve,cur2);
            }
        }
        for(auto x: q) {
            ans -= cost(x.first.first,x.first.second,x.second);
            ans %= MOD;
        }
        printf("%lld\n",(ans%MOD+MOD)%MOD);
    }
    return 0;
}
