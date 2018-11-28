/**         
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 * Date: 2014.06.14
 */

#include <cstdio>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define zero(a) memset(a, 0, sizeof(a))
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()

typedef vector <int> vi;

const int N = 10100;

int mi, n, id[N];
char type[N];

void go( int i, set <int> &in, set <int> &out, int extra )
{
  if (i == n)
  {
    mi = min(mi, sz(in) + extra);
    return;
  }
  if (type[i] == 'E')
    if (id[i] == 0)
    {
      vector <int> v(all(out));
      for (auto x : v)
      {
        assert(!in.count(x));
        in.insert(x);
        out.erase(x);
        go(i + 1, in, out, extra);
        out.insert(x);
        in.erase(x);
      }
      go(i + 1, in, out, extra + 1);
    }
    else
    {
      if (in.count(id[i]))
        return;
      int was = out.count(id[i]);
      in.insert(id[i]);
      if (was)
        out.erase(id[i]);
      go(i + 1, in, out, extra);
      in.erase(id[i]);
      if (was)
        out.insert(id[i]);
    }
  else 
    if (id[i] > 0)
    {
      if (out.count(id[i]))
        return;
      out.insert(id[i]);
      if (in.count(id[i]))
      {
        in.erase(id[i]);
        go(i + 1, in, out, extra);
        in.insert(id[i]);
      }
      else 
      {
        if (extra)
          go(i + 1, in, out, extra - 1);
        go(i + 1, in, out, extra);
      }
      out.erase(id[i]);
    }
    else
    {
      go(i + 1, in, out, extra);
      if (extra)
        go(i + 1, in, out, extra - 1);
      vector <int> v(all(in));
      for (auto x : v)
      {
        assert(!out.count(x));
        in.erase(x);
        out.insert(x);
        go(i + 1, in, out, extra);
        in.insert(x);
        out.erase(x);
      }
    }
}

void solve()
{
  scanf("%d", &n);
  forn(i, n)
    scanf(" %c%d", &type[i], &id[i]);

  mi = n + 1;
  set <int> in, out;
  go(0, in, out, 0);
  if (mi > n)
    puts("CRIME TIME");
  else
    printf("%d\n", mi);
}

int main()
{
  int tn;
  scanf("%d", &tn);
  forn(t, tn)
  {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
