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
int T,X,R,C;

int res() {
    //if(R*C%X == 0 )return 0;
    //return 1;
    if(X==1) return 0; //GABRIEL
    if(X==2) {
        if(R*C % 2 == 0) return 0;
        else return 1;
    }
    if(X==3) {
        if(R==1 || C==1) return 1;
        if(R*C % 3 == 0) return 0;
        else return 1;

    }
    if(X==4) {
        if(R==1 || C==1) return 1;
        if(R*C<=8) return 1;
        if(R*C%4 != 0) return 1;
        return 0;

    }

}

int main() {
  scanf("%d",&T);
  FOR(TTT,1,T) {
    scanf("%d %d %d",&X,&R,&C);
    printf("Case #%d: %s\n",TTT,res() ? "RICHARD" : "GABRIEL");
  }
  return 0;
}
