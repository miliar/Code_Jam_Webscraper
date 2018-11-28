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

int T;
int D;
int a[1010];
int x;
priority_queue<int> q;

int ile(int x) {
    int res = 0;
    FOR(i,1,D) {
        res += MAX((a[i]+x-1)/x - 1,0);
    }
    return res;
}

int main() {
  scanf("%d",&T);
  FOR(TTT,1,T) {
    scanf("%d",&D);
    //q = priority_queue<int>();
    int minn = 1000000;
    FOR(i,1,D) {
        scanf("%d",&a[i]);
    }

    FOR(i,1,1000) {
        minn = MIN(minn,i+ile(i));
    }
    printf("Case #%d: %d\n",TTT,minn);
  }
  return 0;
}
