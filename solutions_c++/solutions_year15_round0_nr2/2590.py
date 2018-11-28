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

vi primes;


int test(int i, int eaten, vi& pancakes)
{
   while (i - eaten >= 0 && pancakes[i] == 0)
      i--;
   int numcakes = i - eaten;
   if (numcakes <= 0)
      return 0;
   if (numcakes <= 3)
      return numcakes;
   if (numcakes % 2 != 0)
   {
      //return test(i, eaten + 1, pancakes) + 1;
      int backupi = pancakes[i - (numcakes / 2)];
      int backupi2 = pancakes[i];
      int backupi3 = pancakes[i - (numcakes / 2) - 1];

      //int ifeaten = test(i, eaten + 1, pancakes) + 1;
      int ifeaten = numcakes;
      pancakes[i - (numcakes / 2)] += pancakes[i];
      pancakes[i - (numcakes / 2) - 1] += pancakes[i];
      pancakes[i] = 0;
      int special = test(i - 1, eaten, pancakes) + backupi2;
      pancakes[i - (numcakes / 2)] = backupi;
      pancakes[i] = backupi2;
      pancakes[i - (numcakes / 2) - 1] = backupi3;
      return min(special, ifeaten);

   }
   else
   {
      int backupi = pancakes[i - (numcakes / 2)];
      int backupi2 = pancakes[i];
      //int ifeaten = test(i, eaten + 1, pancakes) + 1;
      int ifeaten = numcakes;
      pancakes[i - (numcakes / 2)] += 2 * pancakes[i];
      pancakes[i] = 0;
      int special = test(i - 1, eaten, pancakes) + backupi2;
      pancakes[i - (numcakes / 2)] = backupi;
      pancakes[i] = backupi2;
      return min(special, ifeaten);
   }
   
}

int test2(int i, vi& pancakes)
{
   while (i > 0 && pancakes[i] == 0)
      i--;
   if (i <= 0)
      return 0;
   if (i <= 3)
      return i;
   int ifeaten = i;

   int bkp1 = pancakes[i];
   int bkp2 = pancakes[i / 2];
   int bkp3 = pancakes[i / 2 + 1];

   pancakes[i] = 0;
   pancakes[i / 2] += bkp1;
   if (i % 2 == 0)
      pancakes[i / 2] += bkp1;
   else
      pancakes[i / 2 + 1] += bkp1;

   int ifspecial = test2(i, pancakes) + bkp1;

   pancakes[i] = bkp1;
   pancakes[i / 2] = bkp2;
   pancakes[i / 2 + 1] = bkp3;

   bool found = false;

   for (auto prime : primes)
   {
      if (prime >= i)
      {
         break;
      }
      if (i % prime == 0)
      {
         found = true;
         int bkp1 = pancakes[i];
         int bkp2 = pancakes[i / prime];
         
         pancakes[i] = 0;
         pancakes[i / prime] += bkp1 * prime;

         ifspecial = min(ifspecial, test2(i, pancakes) + bkp1 * (prime - 1));

         pancakes[i] = bkp1;
         pancakes[i / prime] = bkp2;
         break;
      }
      
   }
   
   return min(ifeaten, ifspecial);
}

int main() {
   REP(i, 2, 1000)
   {
      bool prime = true;
      REP(j, 2, (int)sqrt(i)+1)
      {
         if (i % j == 0)
         {
            prime = false;
            break;
         }
      }
      if (prime)
         primes.push_back(i);
   }

   int ntc;
   cin >> ntc;
   FORN(kk, ntc)
   {
      int size;
      cin >> size;
      vi diners(size);
      vi pancakes(1001);

      FORN(i, size)
      {
         cin >> diners[i];
         //cout << diners[i] << ' ';
         pancakes[diners[i]]++;
      }
      //cout << endl;
      vi pc2(pancakes);
      int ans = test2(1000, pancakes);
      bool eq = true;
      FORN(i, pancakes.size())
      {
         if (pancakes[i] != pc2[i])
         {
            eq = false;
            break;
         }
      }
      printf("Case #%d: %d\n", kk + 1, ans);
   }
   return 0;
}
