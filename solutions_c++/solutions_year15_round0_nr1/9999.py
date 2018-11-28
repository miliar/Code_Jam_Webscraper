#include <stdio.h>
#include <iostream>
using namespace std;

int count(int a[],int n)
{
  int stood=0;//already stood
  int sum=0;
  
  for (int i=0; i<=n; ++i)
    {
      if (stood<i && a[i]!=0)
        {
          sum+=i-stood;
          stood+=i-stood;
        }
      stood+=a[i];
    }
    
  return sum;
}


int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);
  
  int T;
  
  scanf("%d",&T);
  for (int i=1; i<=T; ++i)
    {
      char str[1010];
      int a[1010];
      int n;
      
      scanf("%d%s",&n,str);
      for (int j=0; j<=n; ++j)
        a[j]=str[j]-'0';
      
      printf("Case #%d: %d\n",i,count(a,n));
    }

  fclose(stdin);
  fclose(stdout);
  
  return(0);
}
