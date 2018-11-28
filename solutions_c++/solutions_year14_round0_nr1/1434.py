#include <cstdio>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int CARDS = 16;

vector<int> first;
vector<int> second;

set<int> seen;
set<int> solutions;

int main() {
   int n;
   scanf("%d", &n);
   
   for (int t = 1; t <= n; ++t) {
      first.clear();
      second.clear();
      first.resize(CARDS);
      second.resize(CARDS);
      seen.clear();
      solutions.clear();
      
      int row1, row2;
      
      scanf("%d", &row1);
      
      for (int row = 1; row <= 4; ++row) {
         int a[4];
         scanf("%d%d%d%d", a, &a[1], &a[2], &a[3]);
         
         if (row == row1) {
            seen.insert(a, a+4);
         }
      }
      
      scanf("%d", &row2);
      
      for (int row = 1; row <= 4; ++row) {
         int a[4];
         scanf("%d%d%d%d", a, &a[1], &a[2], &a[3]);
         
         if (row == row2) {
            for (int i = 0; i < 4; ++i) {
               if (seen.find(a[i]) != seen.end()) {
                  solutions.insert(a[i]);
               }
            }
         }
      }

      
      if (solutions.size() == 0) {
         printf("Case #%d: Volunteer cheated!\n", t);
      } else if (solutions.size() == 1) {
         printf("Case #%d: %d\n", t, *solutions.begin());
      } else {
         printf("Case #%d: Bad magician!\n", t);
      }
   }
   
   
   
   return 0;
}