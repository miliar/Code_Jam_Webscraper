#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <deque>
#include <numeric>
#include <iterator>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <sys/time.h>

using namespace std;

#define DEBUG(x) cout << #x << ": " << x << endl
#define sz(a) int((a).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
template <typename T> string tostr(const T& t) { ostringstream os; os<<t; return os.str(); }

typedef long long llong;


bool is_vocal(char ch) {
   return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

int main(int argc, char *argv[]) { 
   int TC, N;
   string S;
   cin >> TC;
   for(int tc = 1; tc <= TC; ++tc) {
      cin >> S >> N;
      int res = 0;
      for(int i = 0; i < sz(S); ++i) {
         for(int j = i; j < sz(S); ++j) {
            int cntC = 0;
            bool ok = false;
            for(int k = i; k <= j; ++k) {
               if(!is_vocal(S[k])) cntC++;
               else cntC = 0;
               if(cntC >= N) {
                  ok = true;
                  break;
               }
            }
            if(ok) res++;
         }
      }
      cout << "Case #" << tc << ": " << res << endl;
   }
   return 0;
}
