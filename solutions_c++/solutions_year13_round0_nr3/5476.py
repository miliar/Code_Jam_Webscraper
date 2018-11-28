#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int reverse(int n)
{
  int m=0;
  while(n)
    {
      m=(m*10)+(n%10);
      n/=10;
    }
  return m;
}

int pali(int n)
{
  if(n==reverse(n))
    return 1;
  return 0;
}

int main()
{
  int tc;
  scanf("%d",&tc);
  for(int i=1;i<=tc;i++)
    {
      int a,b;
      scanf("%d%d",&a,&b);
      int counter=0;
      for(int j=a;j<=b;j++)
	{
	  if(j==reverse(j))
	    {
	      int k = (int) sqrt(j);
	      if(j==k*k)
		{
		  if(k==reverse(k))
		    counter++;
		}
	    }
	}
      printf("Case #%d: %d\n",i,counter);
    }
  
}
