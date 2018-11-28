#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
#define N 1000000

int s[N];
int m[N];
int smin[N];
int smax[N];

priority_queue<pair<int, int> > PQ;
priority_queue<int> IN;

int main()
{
  int nb_cas;
  scanf("%d", &nb_cas);
  for(int cas=1;cas<=nb_cas;cas++)
    {
      while(!IN.empty())IN.pop();
      while(!PQ.empty())PQ.pop();
      printf("Case #%d: ",cas);
      // solution
      int n,d;
      scanf("%d%d",&n,&d);
      //fprintf(stderr,"\n n %d d %d\n",n,d);
      int a,c,r;
      scanf("%d%d%d%d",&s[0],&a,&c,&r);
      int a2,c2,r2;
      scanf("%d%d%d%d",&m[0],&a2,&c2,&r2);
      for(int i=1;i<n;i++)
	s[i]=((ull)s[i-1]*a+c)%r;
      for(int i=1;i<n;i++)
	m[i]=((ull)m[i-1]*a2+c2)%r2;
      for(int i=1;i<n;i++)
	m[i]=m[i]%i;
      //done
      smin[0]=s[0];smax[0]=s[0];
      for(int i=1;i<n;i++)
	{
	  smin[i]=min(s[i],smin[m[i]]);
	  smax[i]=max(s[i],smax[m[i]]);
	}
      for(int i=1;i<n;i++)
	PQ.push(make_pair(-1*smax[i],-1*smin[i]));
      int score=0;
      //for(int i=0;i<n;i++)
      //fprintf(stderr,"i%d : s%d smin%d smax%d m%d\n",i,s[i],smin[i],smax[i],m[i]);
      //fprintf(stderr,"yaya\n");
      for(int lb = 0;lb < r;lb++)
	{
	  //fprintf(stderr,"-- %d\n",lb);
	  while(!PQ.empty() && -1*PQ.top().first<=lb+d)
	    {
	      //fprintf(stderr,"get %d %d\n",-1*PQ.top().second,-1*PQ.top().first);
	      IN.push(PQ.top().second);
	      PQ.pop();
	    }
	  while(!IN.empty() && -1*IN.top()<lb)
	    {
	      //fprintf(stderr,"drop %d\n",-1*IN.top());
	      IN.pop();
	    }
	  score=max(score, (int)IN.size());
	}
      printf("%d\n",score+1);
	


	
      // end
    }
  return 0;
}
