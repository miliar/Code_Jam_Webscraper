#include <cstdio>
#include <set>
#include <string>
#include <vector>
//#include <algorithm>
#include <cstdint>


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


int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     forr (tt, 1, T) {

          int64_t k,c,s;
          scanf("%li %li %li\n", &k, &c, &s);

          //printf("(%li %li %li)\n", k, c, s);
          int64_t studs[200];
          int studpos = 0;
          for (int i = 0; i < k; studpos++) {
               int64_t p = i;
               i++;
               for (int j=1;j<c;j++) {
                    p = p * k ;
                    if (i < k) { p += i; i++; }
               }
               studs[studpos] = p + 1;
          }

          printf("Case #%i:", tt);

          if (studpos > s) printf("IMPOSSIBLE");
          else {
               for (int i=0;i<studpos;i++) printf(" %li", studs[i]);
          }


          printf("\n");


     }
}
