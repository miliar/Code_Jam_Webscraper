#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

#define FOR(i,v,n) for(int i=v;i<=n;i++)

int T,N,M;
int a[105][105];
int rowm[105],colm[105];

int main()
{
  cin>>T;

  FOR(t,1,T)
    {
      cin>>N>>M;
      FOR(i,1,100)
	rowm[i]=colm[i]=1;

      FOR(n,1,N)
	FOR(m,1,M)
	{
	  scanf("%d",a[n]+m);
	  rowm[n]=max(rowm[n],a[n][m]);
	  colm[m]=max(colm[m],a[n][m]);
	}
      int poss=1;
      for(int n=1;n<=N && poss;n++)
	for(int m=1;m<=M && poss;m++)
	{
	  if(rowm[n]!=a[n][m] && colm[m]!=a[n][m])
	    poss=0;
	}
      printf("Case #%d: %s\n",t,(poss?"YES":"NO"));
    }
  return 0;
}
