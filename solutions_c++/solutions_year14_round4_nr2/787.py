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
int tttt,q;
vector<int> v;
//vector<PII> w[1010];
int n;
int a[1010][1010];

map<int,int> pos,pos2;
int go(int pr, int suf, int pos) {
    return 0;
}

int main() {
  scanf("%d",&tttt);
  FOR(ttt,1,tttt) {
    v.clear();
    pos.clear(); pos2.clear();
    CLEAR(a);
    scanf("%d",&n);
    FOR(i,1,n) {scanf("%d",&q); v.PB(q); pos[q] = i;}
    sort(v.begin(),v.end());

    FOR(i,1,n) {
        int zos = n-i+1;
        int r = pos[v[i-1]];
        FOR(m,0,i) {
            int p = m;
            int q = i-m;
            if(p == 0) a[p][q] = a[p][q-1] + zos-r;
            else if(q==0) a[p][q] = a[p-1][q] + r-1;
            else a[p][q] = MIN(a[p-1][q] + (r-1),a[p][q-1] + (zos - r));
            //if(p-1 >= 0) a[p][q] = a[p-1][q] + (r-1);


            //printf("%d %d %d %d %d\n",p,q,a[p][q],r,zos);
        }
        pos.erase(v[i-1]);
        FOREACH(it,pos) if(it->ND > r) {
            //printf("%d %d %d\n",it->ST,it->ND,r);
            pos[it->ST]--;
        }
        //pos = pos2;
    }
    int res = 10000000;
    FOR(i,0,n) {
        int p = i;
        int q = n-i;
        res = MIN(res,a[p][q]);
    }
    printf("Case #%d: %d\n",ttt,res);
  }
  return 0;
}
