#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


int main()
{
  int  T,N,J;
  int  count=0;
  scanf("%d",&T);
  // fill_com(15);
  for(int i=1;i<=T;++i)
  {
    printf("Case #%d:\n", i);
    scanf("%d%d",&N,&J);
     for(int odd1=1;odd1<=30;odd1+=2)
       for(int odd2=odd1+2;odd2<=30;odd2+=2)
      for(int even1=2;even1<=30;even1+=2 )
	for(int even2=even1+2;even2<=30;even2+=2 )
	{
	  if(count==500) break;
	  printf("1");
	  for(int j=1;j<=30;++j)
	    {
	      if(j==odd1||j==odd2||j==even1||j==even2) printf("1");
	      else printf("0");
	    }
	  printf("1 ");
	  for(int j=2;j<=10;++j) printf(" %d",j+1);
	  printf("\n");
	  count++;
	} 
   } 
  return 0;
}
