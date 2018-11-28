#include <bits/stdc++.h>

using namespace std;

const int INF = 1000000000;
const int N = 16;

int n, m;
bool t[N][N];
int score;

void actu()
{
   int r = 0;
   for(int lin=0; lin<n; lin++)
      for(int col=0; col<m; col++)
         if(t[lin][col])
         {
            if(lin < n-1)
               r += t[lin+1][col];
            if(col < m-1)
               r += t[lin][col+1];
         }
   score = min(score, r);
}

void f(int lin, int col, int x)
{
   if(lin == n)
   {
      if(x == 0)
         actu();
      return;
   }
   if(col == m)
   {
      f(lin+1, 0, x);
      return;
   }
   f(lin, col+1, x);
   t[lin][col] = true;
   f(lin, col+1, x-1);
   t[lin][col] = false;
}

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      int x;
      cin >> n >> m >> x;
      score = INF;
      f(0, 0, x);
      printf("Case #%d: %d\n", test, score);
   }
   return 0;
}