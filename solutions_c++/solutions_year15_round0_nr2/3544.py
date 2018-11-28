#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;


int main()
{
  int nbcases;
  scanf("%d",&nbcases);
  for(int cas = 0; cas < nbcases; cas++)
  {

    int d;
    vector<int> valeurs;
    scanf("%d",&d);
    int maxi=0;
    for(int i = 0; i < d; i++)
    {
      int v;
      scanf("%d",&v);
      valeurs.push_back(v);
      maxi = max(maxi, v);
    }
    int debut = 1;
    int fin = 1001;
    int mini = 1000;
    for(int test = 1; test <= 1000; test++)
    {
      int resultat = 0;
      for(int i = 0; i < d; i++)
      {
	resultat += (valeurs[i] + test - 1) / test - 1;
      }
      mini = min(mini, resultat + test);
    }
    printf("Case #%d: %d\n", cas+1, mini);

  }
  return 0;
}
