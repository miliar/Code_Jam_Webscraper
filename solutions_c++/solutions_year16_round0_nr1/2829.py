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

LL T,N,k,c;
LL res,mask;

int main() {
  cin >> T;
  FOR(iiii,1,T) {
    cin >> N;
    if(N==0)
    {
        cout << "Case #" << iiii << ": INSOMNIA\n";
    }
    else {
        k = 1;
        mask = 0;
        while(1)
        {
            c = k*N;
            //cout << c << "\n";
            while(c > 0)
            {
                mask |= (1<<(c%10));
                c/=10;
            }

            if(mask == 1023)
            {
                res = k*N;
                break;
            }

            k++;
        }
        cout << "Case #" << iiii << ": " << res << "\n";
    }
  }

  return 0;
}
