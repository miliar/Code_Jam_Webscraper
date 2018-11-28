#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <cassert>
#include <complex>
#include <climits>
#include <functional>

using namespace std;

#define ST first
#define ND second
#define MP make_pair
#define PB push_back


typedef unsigned int uint;
typedef long long LL;
typedef long double LD;

typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))

#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl


int main(int argc, char **argv)
{

   int testcases, M, N;

   cin >> testcases;

   int map[100][100];

   for (int caso = 1; caso <= testcases; ++caso)
   {
      cin >> N;cin >> M; 
      bool could = true;
      for (int i =0; i < N ; i ++) {
         for (int j = 0; j < M; j++)
         {
            cin >> map[i][j];
         }
      }
      for (int i =0; i < N && could; i ++) {
         for (int j = 0; j < M && could; j++)
         {
            bool vert = true;
            bool horz = true;
            for (int k = 0; k < N; k++)
               if (map[k][j] > map[i][j]) vert = false;

            for (int k = 0; k < M; k++)
               if (map[i][k] > map[i][j]) horz = false;

            if (!vert && !horz) could = false;
         }
      }

      if (could)
         cout << "Case #" << caso << ": YES" <<  endl;
      else
         cout << "Case #" << caso << ": NO" <<  endl;
      
   }

}