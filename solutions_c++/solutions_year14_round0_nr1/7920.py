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
int n;
int a[20][20];
int r[20];
int main() {
  scanf("%d",&n);
  FOR(ttt,1,n) {
    int rown;
    FOR(i,1,20) r[i]=0;

    FOR(t,1,2) {
        scanf("%d",&rown);
        FOR(i,1,4) FOR(j,1,4) {
            scanf("%d",&a[i][j]);
            if(i == rown) r[a[i][j]]++;
        }
    }
    vector<int> v;
    FOR(i,1,16) {
        if(r[i] == 2) v.PB(i);
    }

    if(SZ(v) == 1) {
        printf("Case #%d: %d\n",ttt,v[0]);
    }
    else if(SZ(v) >= 2) {
        printf("Case #%d: Bad magician!\n",ttt);
    }
    else {
        printf("Case #%d: Volunteer cheated!\n",ttt);
    }
  }

  return 0;
}
