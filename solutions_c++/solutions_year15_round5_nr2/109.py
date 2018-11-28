#include<bits/stdc++.h>
using namespace std;

#define N 10000
int s[N];
int x[N];
int lo[N];int hi[N];

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	int n,k;
	scanf("%d%d",&n,&k);
	int S=n-k+1;
	for(int i=0;i<S;i++)
	  scanf("%d",&s[i]);
	//
	for(int i=0;i<k;i++)x[i]=0;
	for(int i=k;i<n;i++)x[i]=x[i-k]+s[i-k+1]-s[i-k];
	// for(int i=0;i<n;i++)
	//   printf("%d ",x[i]);
	// printf("\n");
	int diff=0;
	for(int c=0;c<k;c++)
	  {
	    lo[c]=x[c],hi[c]=x[c];
	    int i=0;
	    while(c+i*k<n)
	      {
		lo[c]=min(lo[c],x[c+i*k]);
		hi[c]=max(hi[c],x[c+i*k]);
		i++;
	      }
	    i=0;
	    while(c+i*k<n)
	      {
		x[c+i*k]-=lo[c];
		i++;
	      }
	    diff=max(diff,hi[c]-lo[c]);
	    hi[c]-=lo[c];
	  }

	int allhi=hi[0];
	for(int i=0;i<k;i++)allhi=max(allhi,hi[i]);
	int margin=0;
	for(int i=0;i<k;i++)
	  margin+=allhi-hi[i];
	int ret=0;
	int mys0=0;
	for(int i=0;i<k;i++)mys0+=x[i];
	mys0=mys0%k;
	int div=(1000000*k+s[0]-mys0)%k;
	//printf("div %d\n",div);
	//if(div<0)printf("%d %d %d %d\n",n,k,s[0],mys0);
	if(div>margin)ret=1;
	
	// for(int i=0;i<n;i++)
	//   printf("%d ",x[i]);
	// printf("\n");
	printf("%d\n",diff+ret);
	// end
    }
    return 0;
}
