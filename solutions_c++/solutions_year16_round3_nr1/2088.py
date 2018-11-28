#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int tabe(int *tab)
{
  for (size_t i = 0; i < 26; i++) {
    if (tab[i] != 0)
      return (0);
  }
  return 1;
}

int getmax(int *tab)
{
    int i = 0;
    int tmp = -1;
    int itmp = -1;

    while (i < 26)
    {
      if (tab[i] > tmp && tab[i] != 0)
        {
          itmp = i;
          tmp = tab[i];
        }
        i++;
    }
    return itmp;
}

int nbrleftat1(int *tab)
{
  int i = 0;
  int tmp = 0;

  while (i < 26)
  {
    if (tab[i] == 1)
      tmp++;
    if (tab[i] > 1)
      return (-1);
    i++;
  }
  return tmp;
}

int main() {
  int t, n, m;
  int tab[26];
  char *alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  cin >> t;
  int k = 0;
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    k = 0;
    memset(tab, 0, sizeof(tab));
    for (int j = 0; j < n; j++) {
      cin >> tab[k];
      k++;
    }
    cout << "Case #" << i << ": ";
    int l;
    int f;
    f = 0;
    while ((l = getmax(tab)) != -1)
    {
      cout << alph[l];
      tab[l] = tab[l] - 1;
      int g = nbrleftat1(tab);
      if (g == 2)
      {
      //  if ((f - 1) % 2 != 1)
          cout << " ";
        int o = getmax(tab);
        cout << alph[o];
        tab[o]--;
        o = getmax(tab);
        cout << alph[o];
        break;
      }
      if (f % 2 == 1)
        cout << " ";
      f++;
    }
    cout << endl;
  }
  return 0;
}
