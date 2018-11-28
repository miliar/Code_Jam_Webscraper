#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <queue>

#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cstdio>

using namespace std;
const int MAXN = 1000;
int grid[MAXN][MAXN];
int N,M;

vector<int> getVertical(int col)
{
   vector<int> v;
   for(int row = 0; row < N; row++) v.push_back(grid[row][col]);
   return v;
}

vector<int> getHorizontal(int row)
{
   vector<int> v;
   for(int col = 0; col < M; col++) v.push_back(grid[row][col]);
   return v;
}

int valid(const vector<int> &v, int value)
{
   for(int i = 0; i < v.size(); i++) if(v[i] > value) return 0;
   return 1;
}
int isok()
{
   int cnt = 0;
   for(int row = 0; row < N; row++) {
      for(int col = 0; col < M; col++) {
          vector<int> v1 = getVertical(col);
          vector<int> v2 = getHorizontal(row);
          if(valid(v1,grid[row][col])||valid(v2,grid[row][col])) cnt++;
      }
   }
   return (cnt == N*M);

}
int main()
{
   freopen("B-large.in","r",stdin);
   freopen("B-large.txt","w",stdout);
   int T;
   scanf("%d",&T);
   for(int tc = 1; tc <= T; tc++) {
      scanf("%d %d",&N,&M);
      for(int i = 0; i < N; i++) {
         for(int j = 0; j < M; j++) {
            scanf("%d",&grid[i][j]);
         }
      }

      int ok = isok();
      printf("Case #%d: ",tc);
      if(ok) printf("YES");
      else printf("NO");
      printf("\n");


   }
   return 0;
}
