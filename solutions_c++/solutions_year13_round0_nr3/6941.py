#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(__typeof(c.begin()) i=(c.begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define ZERO(x) memset(x,0,sizeof(x))

void alg() {
   int tab[7], a, b ,p1,p2;
    static int caseNo = 0;
   p1=0;
   p2=0;
   tab [0]=1;
      tab[1]= 4;
      tab[2]=9;
      tab[3]= 121;
      tab[4] = 484;
      tab[5] = 10001;
      cin >> a >> b ;

      int i;
      i=0;
      while (a>tab[i]) {
      p1= i+1;
      i++;
      }
      i=0;

      while (b>=tab[i]) {
      p2=i+1;
      i++;
      }


      int result = p2- p1 ;
       cout << "Case #" << ++caseNo << ": " << result << endl;
    }

    
    
int main() {
    int nCases;
    cin >> nCases;

    for (int i = 0; i < nCases; ++i) {
        alg();
    }
 return 0;   
}
                  

                  

