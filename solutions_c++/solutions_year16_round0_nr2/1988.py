#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


char seq[110];

int main()
{
  int  T;
  scanf("%d",&T);
  // fill_com(15);
 
  for(int i=1;i<=T;++i)
  {
    printf("Case #%d: ", i);
    scanf("%s",seq);
    int len=strlen(seq);
    int ans=0;
    char cmp='+';
    for(int j=len-1;j>=0;--j)
    {
      if(seq[j]!= cmp)
       {
	 ++ans;
	 cmp=seq[j];
	}
      
    }
    printf("%d\n",ans);
   } 

  return 0;
}
