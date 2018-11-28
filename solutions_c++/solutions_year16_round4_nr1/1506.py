#include <bits/stdc++.h>
using namespace std;

int a[1<<13];

int w[] = { 0, 0, 2, 1 };

int Go (int r, int p, int s, int i)
{
  int j;
  if (r < 0 || p < 0 || s < 0) return 0;
  if (!r && !p && !s) return 1;
  for (a[i] = 0; a[i] < 3; a[i]++) {
    for (j = i; j > 1 && (j & 1) && a[j] != a[j-1]; j >>= 1) a[j>>1] = w[a[j]+a[j-1]];
    if ((j == 1 || !(j & 1)) && (a[i] == 0 ? Go (r,p-1,s,i+1) : a[i] == 1 ? Go (r-1,p,s,i+1) :
        Go (r,p,s-1,i+1))) return 1;
  }
  return 0;
}

int main ()
{
  int t, i;
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
/*    vector<int> k;
    for (int j = 0; j < 5; j++) k.push_back (j + j + 1);
    do {
      for (auto &j : k) printf ("%d ", j);
      printf ("\n");
    } while (next_permutation (k.begin(), k.end())); */
    
    int n, r, p, s;
    scanf ("%d%d%d%d", &n, &r, &p, &s);
    printf ("Case #%d: ", i);
    if (!Go (r, p, s, 1<<n)) printf ("IMPOSSIBLE\n");
    else {
      for (r = (1<<n); r < (2<<n); r++) printf ("%c", "PRS"[a[r]]);
      printf ("\n");
    }
  }
  return 0;
}
