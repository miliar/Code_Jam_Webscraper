#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <iterator>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cassert>

using namespace std;
set<int> grid1[4];
set<int> grid2[4];

void fillGrid(set<int> grid[])
{

   for(int row = 0; row < 4; row++) {
         grid[row].clear();
      for(int col = 0; col < 4; col++) {
         int v;
         cin>>v;
         grid[row].insert(v);
      }
   }
}

string solve(int row1, int row2)
{

   set<int> intersectSet;
   set_intersection(grid1[row1].begin(), grid1[row1].end(),
      grid2[row2].begin(), grid2[row2].end(), inserter(intersectSet, intersectSet.begin()));
   ostringstream oss;
   int size = intersectSet.size();
   if(size == 1) {
      oss<<*(intersectSet.begin());
   }else if(size > 1) {
      oss<<"Bad magician!";
   }else {
      oss<<"Volunteer cheated!";
   }
   return oss.str();

}
int main()
{

   freopen("A-small-attempt0.in", "r", stdin);
   freopen("A-small.out", "w", stdout);

   int T;
   cin>>T;
   for(int tc = 1; tc <= T; tc++) {
      int row1, row2;
      cin>>row1;
      fillGrid(grid1);
      cin>>row2;
      fillGrid(grid2);

      cout<<"Case #"<<tc<<": "<<solve(row1-1, row2-1)<<endl;
   }

   return 0;
}

