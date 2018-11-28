#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

bool richwin(int x,int r,int c)
{
  if((r*c)%x != 0) return true;  
  if (x<=2) return false;
  if(x==3) return (r==1 || c==1);
  if(x==4) return (r<3 || c<3);
}

  
int main()
{
  int nbcas;
  scanf("%d",&nbcas);
  for(int cas=0;cas<nbcas;cas++)
    {
      printf("Case #%d: ",cas+1);
      int x,r,c;
      scanf("%d%d%d",&x,&r,&c);
      if(richwin(x,r,c))
	printf("RICHARD\n");
      else
	printf("GABRIEL\n");
      //printf("%d%d%d\n",x,r,c);
    }
}
