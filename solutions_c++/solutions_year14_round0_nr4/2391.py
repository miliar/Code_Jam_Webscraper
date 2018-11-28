#include <cstdio>
#include <algorithm>

#define LSE ra+=0
#define WIN ra+=1

using namespace std;

long int ra,rb;
int st,n,aB,aE,bB,bE;
double A[100002],B[100002];

void calc(int a, int b)
{
  if (A[a]>B[b])
    WIN;
  else if (A[a]<B[b])
    LSE;
}

void operate()
{
  while(aE!=aB)
    {
      if (A[aE]>B[bE])
	{
	  WIN;
	  --aE;--bE;
	}
      else if (A[aE]>B[bE])
	{
	  LSE;
	  --bE;++aB;
	}
      else
	{
	  if (A[aB]>B[bB])
	    {
	      WIN;
	      ++aB;++bB;
	    }
	  else
	    {
	      calc(aB,bE);
	      ++aB;--bE;
	    }
	}
    }
  calc(aE,bE);
}

int main()
{
  scanf("%d",&st);
  for(int s=1;s<=st;++s)
    {
      printf("Case #%d: ",s);
      ra=rb=0;
      scanf("%d",&n);
      for(int i=0;i<n;scanf("%lf",&A[i++]));
      for(int i=0;i<n;scanf("%lf",&B[i++]));
      sort(A,A+n);
      sort(B,B+n);
      aB=bB=0;
      aE=bE=n-1;
      operate();
      rb=ra;
      for(int i=0;i<n;++i)
	swap(A[i],B[i]);
      aB=bB=0;
      aE=bE=n-1;
      ra=0;
      operate();
      printf("%ld %ld\n",rb,n-ra);
    }
  return 0;
}
