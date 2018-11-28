#include <cstdio>
#include <algorithm>

using namespace std;


int main()
{
  int nbcases;
  scanf("%d",&nbcases);
  for(int cas = 0; cas < nbcases; cas++)
  {
    int smax;
    scanf("%d", &smax);
    char temp[1002];
    scanf("%s", temp);
    int resultat = 0;
    int nbgens = 0;
    for(int i = 0; i <= smax; i++)
    {
      if(resultat + nbgens < i)
      {
	resultat += i - resultat - nbgens;
      }
      nbgens += temp[i] - '0';
    }
    printf("Case #%d: %d\n", cas+1, resultat);
  }
  return 0;
}
