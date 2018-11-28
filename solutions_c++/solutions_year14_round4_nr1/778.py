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
int N,X,a;
int f[100100];
set<pair<int,int> > s,r;
int cnt = 0;
int main() {
  scanf("%d",&tttt);
  FOR(ttt,1,tttt) {
    scanf("%d %d",&N,&X);
    s.clear(); r.clear();
    cnt = 0;
    FOR(i,1,N) {
        scanf("%d",&f[i]);
        s.insert(MP(f[i],i));
        r.insert(MP(-f[i],i));
    }

    while(!s.empty()) {
        PII p = *(s.begin());
        s.erase(p);
        PII q = MP(-p.ST,p.ND);
        r.erase(q);

        while(!r.empty()) {
            PII t = *(r.begin());
            r.erase(t);
            PII t2 = MP(-t.ST,t.ND);
            s.erase(t2);
            if(-t.ST + p.ST <= X) break;
            else cnt++;
        }
        cnt++;
    }
    printf("Case #%d: %d\n",ttt,cnt);
  }
  return 0;
}
