#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int t[1000];
int n;

void swa(int i, int j)
{
  //printf("s %d %d\n",i,j);
  t[i] = t[i] + t[j];
  t[j] = t[i] - t[j];
  t[i] = t[i] - t[j];
  return;
}

int main()
{
  int nb_cas;
  scanf("%d",&nb_cas);
  for(int cas = 1; cas <= nb_cas; cas++)
    {
      printf("Case #%d: ",cas);
      scanf("%d",&n);
      for(int i = 0;i<n;i++)
	{scanf("%d",&t[i]);}
      int score=0;
      int a=0;
      int b=n-1;
      for(int i = 0;i<n;i++)
	{
	  int pmin=0;
	  int mi=1000000004;
	  for(int j=a;j<=b;j++)
	    if(t[j]<mi)
	      {mi=t[j];pmin=j;}
	  if(pmin-a < b-pmin)
	    {
	      for(int j = a; j < pmin; j++)
		{swa(j,pmin);score++;}
	      a++;
	    }
	  else
	    {
	      for(int j = b; j > pmin; j--)
		{swa(j,pmin);score++;}
	      b--;
	    }
	  /*
	  for(int j=0;j<n;j++)
	    printf("%d ",t[j]);
	  printf("(%d %d . %d %d)\n",a,b,mi,pmin);
	  */
	}
      printf("%d\n",score);
      
    }
  return 0;
}
