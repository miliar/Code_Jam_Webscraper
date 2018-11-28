#include <cstdio>
#include <set>
#include <string>
//#include <algorithm>
#include <vector>

using namespace std;
//--common
#define forr(i,f,t) for (int i = (f); i <= (t); i++)
#define fori(i,t) for (int i = 0; i < (t); i++)
#define forc(i,c) for (int i = 0; i < (c).size(); i++)
#define forit(it,c) for (auto it = (c).begin(), end = (c).end(); it != end; ++it)

template <typename C> void rerase(C& s, const typename C::const_reverse_iterator &it ) { s.erase(s.find(*it)); }
template <typename T> vector<T>& operator<<(vector<T>& v, const T& t) { v.push_back(t); return v; }
template <typename T> set<T>& operator<<(set<T>& v, const T& t) { v.insert(t); return v; }
//--end common

#include "QList"
#include "QPair"

typedef long long int ll;

int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     forr (tt, 1, T) {
          vector<vector<char> > grid;
          char line[100];
          int r, c;
          scanf("%i %i\n", &r, &c);
          for (int i=0;i<r;i++) {
               scanf("%s\n", line);
               vector<char> x; x.resize(c);
               fori(j,c) x[j] = line[j];
               grid.push_back(x);
          }
          int res = 0;
          fori(i0, r) if (res >= 0) fori(j0,c) {
               //printf(":: %c\n", grid[i0][j0]);
               if (grid[i0][j0] == '.') continue;
               int di = 0, dj = 0;
               int i = i0, j = j0;
               if (grid[i][j] == '^') di = -1;
               if (grid[i][j] == 'v') di = +1;
               if (grid[i][j] == '<') dj = -1;
               if (grid[i][j] == '>') dj = +1;

               i += di;
               j += dj;
               while (i >= 0 && j >= 0 && i < r && j < c && grid[i][j] == '.') {
                    i += di;
                    j += dj;
               }
               //printf("%i %i -> %i %i\n",i0,j0,i,j);
               if (!(i >= 0 && j >= 0 && i < r && j < c)) {
                    i = i0; j = j0;
                    bool ok = false;
                    for (int k = j0 - 1; k >= 0 && !ok; k-- )
                         if (grid[i][k] != '.') {ok = true;break; }
                    for (int k = j0 + 1; k < c && !ok; k++ )
                         if (grid[i][k] != '.') {ok = true;break; }
                    for (int k = i0 - 1; k >= 0 && !ok; k-- )
                         if (grid[k][j] != '.') {ok = true;break; }
                    for (int k = i0 + 1; k < r && !ok; k++ )
                         if (grid[k][j] != '.') {ok = true; break; }
                    if (!ok) { res = -1; break; }
                    else res++;
               }

                    }

          printf("Case #%i: ", tt);
          if (res >= 0) printf("%i\n", res);
          else printf("IMPOSSIBLE\n");
          //printf("%i %i\n", deceiveScore, warScore);
     }
    // for (int i=3;basecache[i];i++)
    //      printf("%lli\n", basecache[i]);
}
