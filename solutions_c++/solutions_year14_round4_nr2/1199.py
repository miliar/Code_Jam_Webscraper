#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>

using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;

ll a[1002];
ll b[1002];
ll c[1002];

template<typename l>
void mergesort(int s, int e, ll & res, l op)
{
  if (s >= e - 1)
    return;

  int mid = (s + e) / 2;

  mergesort(s, mid, res, op);
  mergesort(mid, e, res, op);

  int i = s, j = mid;
  int ind = s;

  while (i < mid || j < e)
  {
    if (i == mid)
    {
      c[ind++] = b[j++];
    }
    else if (j == e)
    {
      c[ind++] = b[i++];
    }
    else if (op(b[i],b[j]))
    {
      c[ind++] = b[i++];
    }
    else
    {
      c[ind++] = b[j++];
      res += mid - i;
    }
  }

  for (i = s; i < e; ++i)
    b[i] = c[i];
}

int main()
{
  freopen("B-small-attempt1.in", "r", stdin);
  freopen("B-result-small-brute1.txt", "w", stdout);
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i)
  {
    int n;
    scanf("%d", &n);
    for (int i =0; i < n; ++i)
      scanf("%I64d", &a[i]);

    //ll x = 0;
    //mergesort(0, n, x, [](ll a1, ll a2) {return a1 <= a2;});
    //for (int i =0; i < n; ++i)
    //  printf("%I64d ", b[i]);
    //printf("\n%lld\n", x);
    //continue;

    //ll max_el = a[0];
    //int max_pos = 0;

    //for (int i = 0; i < n; ++i)
    //{
    //  if (a[i] > max_el)
    //  {
    //    max_el = a[i];
    //    max_pos = i;
    //  }
    //}

    //for (int i = max_pos; i < n - 1; ++i)
    //  a[i] = a[i + 1];
    //--n;

    //ll best = 1000000000;
    //for (int i = 0; i < n + 1; ++i)
    //{
    //  ll cur_res = abs(max_pos - i);

    //  for (int j = 0; j < n; ++j)
    //    b[j] = a[j];

    //  mergesort(0, i, cur_res, [](ll a1, ll a2) {return a1 <= a2;});
    //  mergesort(i, n, cur_res, [](ll a1, ll a2) {return a1 >= a2;});
    //  if (cur_res < best)
    //    best = cur_res;
    //}

    ll best = 100000000;

    for (int i = 0; i < n; ++i)
      b[i] = a[i];
    sort(b, b + n);
    do 
    {
      int i = 0;
      while (i < n - 1 && b[i] < b[i + 1])
        ++i;

      while (i < n - 1 && b[i] > b[i + 1])
        ++i;
      if (i != n - 1)
        continue;

      int cur_res = 0;
      for (int i = 0; i < n; ++i)
      {
        c[i] = a[i];
      }

      for (int i = 0; i < n; ++i)
      {
        for (int j = i; j < n; ++j)
        {
          if (b[i] == c[j])
          {
            while (j > i)
            {
              swap(c[j], c[j-1]);
              ++cur_res;
              --j;
            }
            break;
          }
        }

      }

      if (cur_res < best)
        best = cur_res;
    } while (next_permutation(b, b + n));

    printf("Case #%d: %I64d", i + 1, best);



    printf("\n");
  }

  fclose(stdin);
  fclose(stdout);

  return 0;
}