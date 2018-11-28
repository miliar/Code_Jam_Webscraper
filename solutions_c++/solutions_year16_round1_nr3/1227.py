#include<bits/stdc++.h>
using namespace std;

#define N 1000

int n;
int bff[N];
int cycle[N];
int chain[N];

void f1(int cur, int d0, int d)
{
  if(cycle[cur]==-1)
    {
      cycle[cur]=d;
      f1(bff[cur],d0,d+1);
    }
  else if(cycle[cur]>=d0)
    {
      int taille=d-cycle[cur];
      int pos = cur;
      do
	{
	  cycle[pos]=taille;
	  pos=bff[pos];
	}while(pos!=cur);
    }
  return;
}

void f2(int cur, int d)
{
  if(cycle[cur]!=0)
    chain[cur]=max(chain[cur],d);
  else
    f2(bff[cur],d+1);
}
  
int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	  {
	    int temp;
	    scanf("%d",&temp);
	    bff[i]=temp-1;
	  }
	for(int i=0;i<n;i++)
	  {
	    cycle[i]=-1;
	    chain[i]=0;
	  }
	for(int i=0;i<n;i++)
	  f1(i,(i+1)*N,(i+1)*N);
	for(int i=0;i<n;i++)
	  if(cycle[i]>=N)
	    cycle[i]=0;	
	for(int i=0;i<n;i++)
	  f2(i,0);
	int bestscore=0;
	for(int i=0;i<n;i++)
	  bestscore=max(bestscore,cycle[i]);
	int score2=0;
	for(int i=0;i<n;i++)
	  if(cycle[i]==2)
	    score2+= 1 + chain[i];
	printf("%d\n",max(bestscore,score2));
	  /*
	for(int i=0;i<n;i++)
	  printf("%d ",bff[i]+1);
	printf("\n");
	for(int i=0;i<n;i++)
	  printf("%d ",cycle[i]);
	printf("\n");
	for(int i=0;i<n;i++)
	  printf("%d ",chain[i]);
	printf("\n");
	if(cy)printf("cycle\n");
	else
	  printf("2-cycle\n");
	// end
	if(bestscore>n || bestscore < 2 || (n % 2 == 1 && bestscore == 2))
	exit(2);*/
    }
    return 0;
}
