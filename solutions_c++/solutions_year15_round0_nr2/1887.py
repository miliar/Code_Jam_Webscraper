#include <bits/stdc++.h>
using namespace std;

int niz[1010];
int t, n;

bool cmp(int a, int b)
{
 return a > b;
}

int main()
{
// freopen("t.in", "r", stdin);
// freopen("t.out", "w", stdout);
 scanf("%d", &t);
// printf("100\n");

  for (int j=1; j<=t; j++){
    scanf("%d", &n);
    //printf("%d\n", n);
    int a, b;

    for (int i=1; i<=n; i++)
     scanf("%d", &niz[i]);
    //printf("\n");
    sort(niz+1, niz+1+n, cmp);

    int maxi = niz[1];

    for (int i=(niz[1]-1); i>0; i--)
    {
      int br = 0;
      for (int k=1; k<=n; k++)
        br = br + (niz[k]-1)/i;
      if (i + br < maxi)
        maxi = i + br;
    }

    printf("Case #%d: %d\n", j, maxi);
  }
}
