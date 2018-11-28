//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define CLEAR(x) (memset(x,0,sizeof(x)))
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define VAR(v, n) __typeof(n) v = (n)
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define FOREACH(i, c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define DBG(v) cout<<#v<<" = "<<v<<endl;
#define IN(x,y) ((y).find(x)!=(y).end())
#define ST first
#define ND second
#define PB push_back
#define PF push_front
#define MP make_pair
typedef long long int LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
int tttt;
int m,n;
string s[10];
vector<vector<int> > as;

void gen() {
    //if(SZ(v) == m) return v;
    vector<int> v;
    v.clear();
    vector<vector<int> > res, res2;
    res.PB(v);
    FOR(i,1,m) {
        res2.clear();
        REP(k,SZ(res)) {
            FOR(j,1,n) {
                vector<int> v = res[k];
                v.PB(j);
                res2.PB(v);
            }
        }
        res = res2;
    }
    as = res;
}

int calc(vector<int> v) {
    set<string> ser[6];
    FOR(i,1,m) FOR(j,0,SZ(s[i])) ser[v[i-1]].insert(s[i].substr(0,j));

    int res = 0;
    FOR(i,1,n) res += SZ(ser[i]);
    return res;
}

int ress[1000000];

int main() {
  scanf("%d",&tttt);
  FOR(ttt,1,tttt) {
        scanf("%d %d",&m,&n);
        as.clear();
        FOR(i,1,m) cin >> s[i];
        gen();
        REP(i,SZ(as)) {
            ress[i] = calc(as[i]);
        }
        int maxx = 0;
        REP(i,SZ(as)) {
            maxx = MAX(maxx,ress[i]);
        }
        int cnt = 0;
        REP(i,SZ(as)) if(ress[i] == maxx) cnt++;
        printf("Case #%d: %d %d\n",ttt,maxx,cnt);
  }
  return 0;
}
