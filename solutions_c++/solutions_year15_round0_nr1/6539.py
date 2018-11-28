#include <fstream>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <string>
#include <cmath>
#include <cstring>
#include <cstdio>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> ms;

#define XORSWAP(a, b)   ((a)^=(b),(b)^=(a),(a)^=(b))
#define REP(i, a, b) \
            for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
            for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
            for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
            for (msi::iterator it = (c).begin(); it != (c).end(); it++)

FILE *out;
FILE *in;

void init()
{
    out = fopen("out.txt", "w");
    in = fopen("in.txt", "r");
}

void compute(int smax, char *str, int j)
{
  int total = 0;
  int extra = 0;
  REP(i, 0, smax+1)
  {
    if (total < i)
    {
      extra += (i - total);
      total += (i - total);
    }
    total += (str[i] - '0');
  }
  fprintf(out, "Case #%d: %d\n", j, extra); 
}

int main()
{
  int TC, smax;
  int j = 0;
  char str[1001];
  init();
  fscanf(in,"%d", &TC); // number of test cases
  while (j++ < TC) { 
        fscanf(in,"%d %s",  &smax,str); // compute answer | 6 3
        compute(smax, str,j);
  }
  return 0;
}
