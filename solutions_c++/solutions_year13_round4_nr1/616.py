#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n;

typedef unsigned long long ull;

ull cost(int i, int j) {
   return (j-i)*((ull)(n)) - (j-i-1) * ( (ull) (j-i) ) / 2ULL;
}

int main() {
   int cases;
   scanf("%d",&cases);
   for(int caseno=1;caseno<=cases;caseno++) {
      printf("Case #%d: ",caseno);
      int m;
      scanf("%d %d",&n,&m);
      vector<pair<int,int> > starts(m);
      vector<pair<int,int> > ends(m);
      ull want_total=0;
      for(int i=0;i<m;i++) {
         int ppl;
         scanf("%d %d %d",&starts[i].first,&ends[i].first,&ppl);
         starts[i].second=ends[i].second=ppl;
         want_total+=starts[i].second * cost(starts[i].first, ends[i].first);
      }
      sort(starts.begin(),starts.end());
      sort(ends.begin(),ends.end());
      starts.push_back(make_pair(1000*1000*1000+1,0));
      vector<pair<int,int> > stk;
      unsigned long long total=0;
      int j=0;
      for(int i=0;i<starts.size();i++) {
         // how many people need to stop BEFORE here?
         while(j < ends.size() && ends[j].first < starts[i].first) {

            while (ends[j].second) {
               int amount = min(ends[j].second, stk.back().second);
               total += amount * cost(stk.back().first, ends[j].first);
               stk.back().second -= amount;
               ends[j].second -= amount;
               if (stk.back().second == 0) stk.pop_back();
            }

            j++;
         }
         stk.push_back(starts[i]);
      }
      printf("%lld\n",want_total-total);
   }
   return 0;
}
