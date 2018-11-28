#include<stdio.h>


using namespace std;


int main()
{
  int t, T;
  scanf("%d", &T);
  for(t=0;t<T;t++)
    {
      unsigned A, B, K, i, j, k, count=0;
      scanf("%u %u %u", &A, &B, &K);
      for(i=0;i<A;i++)
	{
	  for(j=0;j<B;j++)
	    {
	      if((i&j) < K)
		count++;
	    }
	}
      printf("Case #%d: %d\n", t+1, count);



    }
}
