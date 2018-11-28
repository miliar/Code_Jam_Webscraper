#include <cstdio>

using namespace std;

int used[16];

int numD(int n)
{
  int num = 0;
  while (n)
    {
      num++;
      n /= 10;
    }
  return num;
}

void addDigits(int n)
{
  while (n)
    {
      used[n%10] = 1;
      n/=10;
    }
}

int main()
{
  int t;
  scanf ("%d",&t);
  for (int T = 1; T <= t; T++)
    {
      int n;
      scanf ("%d",&n);
      printf("Case #%d: ",T);
      if (n==0) printf ("INSOMNIA\n");
      else
	{
	  for (int i=0; i<10; i++) used[i]=0;
	  int numDigits = numD(n),k10=1;
	  for (int i=0; i<numDigits; i++) k10 *= 10;
	  int number = n;
	  while (number <= 11*k10)
	    {
	      addDigits(number);
	      int flag = 1;
	      for (int i=0; i<10; i++)
		if (!used[i]) flag = 0;
	      if (flag)
		{
		  printf ("%d\n",number);
		  break;
		}
	      number += n;
	    }
	}
    }
}
