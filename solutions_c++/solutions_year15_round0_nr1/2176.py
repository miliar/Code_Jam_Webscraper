#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;


char shylevel[2000];

int main()
{
  int nbcas;
  scanf("%d",&nbcas);
  for(int cas=0;cas<nbcas;cas++)
    {
      int n;
      scanf("%d",&n);
      scanf("%s",shylevel);
      int nbpeople = 0;
      int nbfriends = 0;
      for(int i=0;i<=n;i++)
	{
	  //printf("shyness %d nbpeople %d friends %d\n",i,nbpeople,nbfriends);
	  if(nbpeople<i)
	    {
	      nbfriends+=i-nbpeople;
	      nbpeople=i;
	    }
	      
	  nbpeople += shylevel[i]-'0';
	}
      printf("Case #%d: %d\n",cas+1,nbfriends);
    }
}
