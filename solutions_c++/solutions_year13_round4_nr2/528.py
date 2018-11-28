#include <iostream>

#include <cstring>
#include <algorithm>

using namespace std;

typedef long long llong;

#define HIGHESTSETBIT(mask) ( sizeof(long long)*8-1-__builtin_clzll((mask)) )

int N;
llong P;

llong f1() {
   llong nteams = 1LL << N;
   llong lo = 0, hi = nteams-1;
   while (lo < hi) {
      llong mid = lo + (hi-lo+1)/2;
      int nlosses = HIGHESTSETBIT(mid + 1);
      llong m = ((1LL << N)-1) & (~((1LL << (N - nlosses))-1));
      if (m >= P)
         hi = mid-1;
      else
         lo = mid;
   }
   return lo;
}

llong f2() {
   llong nteams = 1LL << N;
   llong lo = 0, hi = nteams-1;
   while (lo < hi) {
      llong mid = lo + (hi-lo+1)/2;
      int nwins = HIGHESTSETBIT(nteams - mid);
      llong m = (1LL << (N - nwins)) - 1;
      if (m >= P)
         hi = mid-1;
      else
         lo = mid;
   }
   return lo;
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      cin >> N >> P;
      llong res1 = f1();
      llong res2 = f2();
      cout << "Case #" << tc << ": " << res1 << ' ' << res2 << endl;
   }

   return 0;
}
