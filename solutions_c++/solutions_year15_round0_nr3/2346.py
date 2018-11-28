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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <assert.h>

#define INF 1023123123
#define EPS 1e-11
#define LSOne(S) (S & (-S))

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define FORB(X,Y) for (int (X) = (Y);(X) >= 0;--(X))
#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define REPB(X,Y,Z) for (int (X) = (Y);(X) >= (Z);--(X))

#define SZ(Z) ((int)(Z).size())
#define ALL(W) (W).begin(), (W).end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

vi pset;
vi cset;
int ndisjoint;
void initSet(int N) { cset = vi(N); pset.assign(N, 0); ndisjoint = N; for (int i = 0; i < N; i++) { pset[i] = i; cset[i] = 1; } }
int findSet(int i) { return pset[i] == i ? i : pset[i] = (findSet(pset[i])); }
bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }
void unionSet(int i, int j) { int pi = findSet(i); int pj = findSet(j); if (pi != pj) { pset[pi] = pj; ndisjoint--; cset[pj] += cset[pi]; } }
int numDisjointSets() { return ndisjoint; }
int sizeOfSet(int i) { return cset[findSet(i)]; }

char calc[300][300][2] = { 0 };

bool algo(string& s, char exp, int start, int end)
{
   char sign = '+';
   char st = s[start];
   for (int i = start + 1; i < end; i++)
   {
      st = calc[st][s[i]][0];
      char newsign = calc[st][s[i]][1];
      if (newsign != sign)
      {
         sign = '-';
      }
      else
      {
         sign = '+';
      }
   }
   return st == exp && sign != '-';
}

char new_sign(char s1, char s2)
{
   if (s1 != s2)
      return '-';
   else
      return '+';
}

int main() {

   calc['1']['1'][0] = '1';
   calc['1']['i'][0] = 'i';
   calc['1']['j'][0] = 'j';
   calc['1']['k'][0] = 'k';

   calc['i']['1'][0] = 'i';
   calc['i']['i'][0] = '1';
   calc['i']['j'][0] = 'k';
   calc['i']['k'][0] = 'j';
   
   calc['j']['1'][0] = 'j';
   calc['j']['i'][0] = 'k';
   calc['j']['j'][0] = '1';
   calc['j']['k'][0] = 'i';

   calc['k']['1'][0] = 'k';
   calc['k']['i'][0] = 'j';
   calc['k']['j'][0] = 'i';
   calc['k']['k'][0] = '1';

   calc['1']['1'][1] = '+';
   calc['1']['i'][1] = '+';
   calc['1']['j'][1] = '+';
   calc['1']['k'][1] = '+';

   calc['i']['1'][1] = '+';
   calc['i']['i'][1] = '-';
   calc['i']['j'][1] = '+';
   calc['i']['k'][1] = '-';

   calc['j']['1'][1] = '+';
   calc['j']['i'][1] = '-';
   calc['j']['j'][1] = '-';
   calc['j']['k'][1] = '+';

   calc['k']['1'][1] = '+';
   calc['k']['i'][1] = '+';
   calc['k']['j'][1] = '-';
   calc['k']['k'][1] = '-';

   int ntc;
   cin >> ntc;
   FORN(kk, ntc)
   {
      int L, X;
      cin >> L >> X;
      string word;
      cin >> word;

      string all;
      FORN(i, X)
      {
         all += word;
      }
      bool found = false;
      char signI = '+';
      char charI = '1';
      int dp[10001] = { 0 };

      for (int i = 0; i < all.size() && !found; i++)
      {
         signI = new_sign(signI, calc[charI][all[i]][1]);
         charI = calc[charI][all[i]][0];
         
         bool ifound = charI == 'i' && signI == '+';
         char signJ = '+';
         char charJ = '1';
         for (int j = i + 1; j < all.size() && ifound && !found; j++)
         {
            signJ = new_sign(signJ, calc[charJ][all[j]][1]);
            charJ = calc[charJ][all[j]][0];
            
            bool jfound = charJ == 'j' && signJ == '+';
            if (jfound && dp[j + 1] == 0)
            {
               char signK = '+';
               char charK = '1';
               for (int k = j + 1; k < all.size() && jfound; k++)
               {
                  signK = new_sign(signK, calc[charK][all[k]][1]);
                  charK = calc[charK][all[k]][0];
               }
               found = jfound && charK == 'k' && signK == '+';
               dp[j + 1] = (charK == 'k' && signK == '+') ? 1 : -1;
            }
            else if (jfound)
            {
               found = jfound && dp[j + 1] == 1;
            }
         }
      }
      printf("Case #%d: %s\n", kk + 1, (found ? "YES" : "NO"));
   }
   return 0;
}
