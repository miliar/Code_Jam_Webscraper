#include <cstdio>
#include <algorithm>
using namespace std;

const int MOD = 1000002013;

struct T{
   long long pos, nb;
   T(long long pos=0, long long nb=0) : pos(pos), nb(nb){}
   bool operator<(const T &t) const
   {
      return pos < t.pos;
   }
};

int main()
{
   int nbTests;
   scanf("%d", &nbTests);
   for(int iTest=1; iTest<=nbTests; iTest++)
   {
      int nbArrets, nbTrajets;
      T debuts[1000], fins[1000];
      scanf("%d%d", &nbArrets, &nbTrajets);
      for(int i=0; i<nbTrajets; i++)
      {
         long long o, e, p;
         scanf("%lld%lld%lld", &o, &e, &p);
         debuts[i] = T(o, p);
         fins[i] = T(e, p);
      }
      long long total = 0;
      for(int i=0; i<nbTrajets; i++)
         total = (total + (debuts[i].nb * ( ( ((fins[i].pos - debuts[i].pos) * nbArrets) - ( (fins[i].pos - debuts[i].pos) * (fins[i].pos - debuts[i].pos - 1) ) / 2 ) % MOD) ) % MOD )% MOD;
      sort(debuts, debuts+nbTrajets);
      sort(fins, fins + nbTrajets); 
      int iDeb = 0;
      long long total2 = 0;
      for(int iFin=0; iFin<nbTrajets; iFin++)
      {
         while(iDeb < nbTrajets - 1 && debuts[iDeb+1].pos <= fins[iFin].pos)
            iDeb++;
         int j = iDeb;
         long long nb = fins[iFin].nb;
         while(nb > 0)
         {
            int diff = min(nb, debuts[j].nb);
            nb -= diff;
            debuts[j].nb -= diff;
            int dist = fins[iFin].pos - debuts[j].pos;
            total2 = (total2 + (diff * ( ( (dist * nbArrets) - ( dist * (dist - 1) ) / 2 ) % MOD) ) % MOD )% MOD;
            j--;
         }
      }
      long long t = (total - total2 + MOD) % MOD;
     // printf("%lld %lld\n", total, total2);
      printf("Case #%d: %lld\n", iTest, t);
   }
   return 0;
}
