#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

//ok, we have to guess the strategies
//for War :
//Ken will always play the one just above, except if he can't then he plays his lowest
//has Naomi any strategy at all ? maybe not, we can try to consider that no, i feel like no
//so we can compute it easily
//for DWar :
//If Naomi wants Ken to play mass mk and win, she will tell mass mk-epsilon
//And in that case Naomi always plays her lowest mass
//So Naomi always plays her lowest mass to remove Ken's highest mass
//or (if she wants to win) she can always tell the truth (or Ken's lowest plus epsilon but no interest)
//not only ! if she has anything higher than Ken's lowest, she can tell more than Ken's highest and win
//est-ce que ca revient pas a reverse les roles ??
//what can Naomi do ? lose her lowest against the highest, win Ken's lowest against her closest high
//Ken can do that when i) Naomi plays her highest ii) Naomi plays her lowest
//if it's irrelevant whether Naomi plays that or differently, it means 
//let's see sur les exemples

//comment on fait pour War ? on trie les deux listes et on fait jouer N par ordre décroissant ou whatever

//seems to work sur les exemples

double na[1000];
double nk[1000];

int main()
{
  int nbcas;
  scanf("%d",&nbcas);
  for(int cas = 1; cas <= nbcas; cas++)
    {
      int n;
      scanf("%d",&n);
      for(int i = 0; i < n; i++)
	scanf("%lf",&na[i]);
      for(int i = 0; i < n; i++)
	scanf("%lf",&nk[i]);
      sort(na,na+n);
      sort(nk,nk+n);
      // first what Naomi wins in War
      int pointwar = 0;
      int pk = 0;
      for(int pn = 0; pn < n; pn++)
	{
	  while(pk < n && na[pn] > nk[pk])
	    pk++;
	  if(pk == n)
	      pointwar++;
	  else
	    pk++;
	}
      // then the reverse
      int pointd = 0;
      pk = 0;
      for(int pn = 0; pn < n; pn++)
	{
	  while(pk < n && nk[pn] > na[pk])
	    pk++;
	  if(pk == n)
	    pointd++;
	  else
	    pk++;
	}
      printf("Case #%d: %d %d\n",cas,n-pointd,pointwar);
    }
  return 0;
}
