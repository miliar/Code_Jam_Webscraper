#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int d;
int p[1000];

int min_stop(int eat)
{
  int stop=0;
  for(int i=0;i<d;i++)
    stop+=((p[i]+eat-1)/eat) - 1;
  return stop;
}
  
int main()
{
  int nbcas;
  scanf("%d",&nbcas);
  for(int cas=0;cas<nbcas;cas++)
    {
      scanf("%d",&d);
      for(int i=0;i<d;i++)
	scanf("%d",&p[i]);
      int mint = 1000;
      for(int eat=1;eat<=1000;eat++)
	mint = min(mint,min_stop(eat)+eat);
      printf("Case #%d: %d\n",cas+1,mint);
    }
}
