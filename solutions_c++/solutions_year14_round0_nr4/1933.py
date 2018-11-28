#include<stdio.h>
#include<algorithm>
#define MAX 1010
using namespace std;

int main()
{
  int i,j,t,k;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
    {
      int n;
      double N[MAX]={0},K[MAX]={0};
      scanf("%d",&n);
      for(j=0;j<n;j++)
	scanf("%lf",&N[j]);
      for(j=0;j<n;j++)
	scanf("%lf",&K[j]);
      sort(N+0,N+n);
      sort(K+0,K+n);
      int war=0,dwar=0,min=0,taken[MAX]={0};
      for(j=n-1;j>=0;j--)
	{
	  int found=0;
	  for(k=min;k<n;k++)
	    if(K[k] > N[j] && taken[k]==0)
	      {
		taken[k]=1;
		found=1;
		break;
	      }
	  if(found==0)
	    {
	      war++;
	      taken[min]=1;
	      min++;
	    }
	}
      min=0;
      int max=n-1;
      for(j=0;j<n;j++)
	{
	  if(N[j]< K[min])
	    {
	      max--;
	    }
	  else
	    {
	      dwar++;
	      min++;
	    }
	}
      printf("Case #%d: %d %d\n\n",i,dwar,war);
    }
  return 0;
}
