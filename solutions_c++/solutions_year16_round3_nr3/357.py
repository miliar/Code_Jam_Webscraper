#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

const int S_MAX = 3;

int J, P, S, K;
int o[3][S_MAX][S_MAX]; //2 parmi 3

vector<array<int, 3>> c;
void g()
{
   c.clear();
   for(int j=0; j<J; j++)
      for(int p=0; p<P; p++)
         for(int s=0; s<S; s++)
            c.push_back({j, p, s});
}

vector<array<int, 3>> bw;
vector<array<int, 3>> w;
void f(int i)
{
   if(i == c.size())
   {
      if(w.size() > bw.size())
         bw = w;
      return;
   }
   int x = c[i][0], y = c[i][1], z = c[i][2];
   bool ok = 1;
   ok &= ++o[0][x][y] <= K;
   ok &= ++o[1][x][z] <= K;
   ok &= ++o[2][y][z] <= K;
   if(ok)
   {
      w.push_back({x, y, z});
      f(i+1);
      w.pop_back();
   }
   o[0][x][y]--;
   o[1][x][z]--;
   o[2][y][z]--;
   f(i+1);
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      cin >> J >> P >> S >> K;
      g();
      f(0);
      cout << "Case #" << test << ": " << bw.size() << endl;
      for(auto x : bw)
      {
         for(auto y : x)
            cout << y+1 << " ";
         cout << endl;
      }
      bw.clear();
   }
   return 0;
}