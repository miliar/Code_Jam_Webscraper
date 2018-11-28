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


int main()
{
  init();
  int TC, i,x,r,c;
  fscanf(in,"%d", &TC); // number of test cases
  while (i++ < TC) 
  { 
    fscanf(in,"%d %d %d", &x, &r, &c); 
    if ((r*c) %x != 0)
      {
        fprintf(out, "Case #%d: %s\n", i, "RICHARD");
      continue ;
      }
    if (x == 3)
    {
      if ((r ==1) | (c == 1))
      {
        fprintf(out, "Case #%d: %s\n", i, "RICHARD");
        continue ;
      }

    }    

    if (x == 4)
    {
      if ((r <= 2) | (c <= 2))
      {
        fprintf(out, "Case #%d: %s\n", i, "RICHARD");
        continue ;
      }



    }
    fprintf(out, "Case #%d: %s\n", i, "GABRIEL");

  }

  return 0;
}
