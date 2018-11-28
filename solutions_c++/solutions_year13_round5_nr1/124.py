# include <cstdio>
# include <cstring>
# include <cmath>
# include <cstdlib>
# include <iostream>
# include <vector>
# include <algorithm>
# include <queue>
# include <set>
# include <map>

using namespace std;

long long ar[37],pref[37];

long double getbest(long long tot,int a,int b)
{
  long long start=max(ar[b-1]-1,ar[a-1]),end=ar[b]-1;
  //printf("%d,%d : %Ld %Ld\n",a,b,start,end);
  if(start>=end)return 0;
  if(start*a+(start+1)*(b-a)>tot+pref[b-1])return 0;
  while(end-start>1)
  {
    long long mid=(start+end)>>1;
    if(mid*a+(mid+1)*(b-a)>tot+pref[b-1])end=mid;
    else start=mid;
  }
  long long useful=start*a-pref[a-1];
  long long used=start*a+(start+1)*(b-a)-pref[b-1];
  //printf("%d,%d : %Ld %Ld %Ld : %.9LE\n",a,b,start,useful,used,useful*(long double)36/a-used);
  return useful*(long double)36/a-used;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    long long B;int N;
    scanf("%Ld%d",&B,&N);

    memset(ar,0,37*sizeof(long long));
    for(int i=0;i<N;i++)
      scanf("%Ld",ar+i);

    sort(ar,ar+37);
    pref[0]=ar[0];
    for(int i=1;i<37;i++)
      pref[i]=pref[i-1]+ar[i];

    long double best=0;
    for(int a=1;a<=36;a++)
      for(int b=a;b<=36;b++)
        best=max(best,getbest(B,a,b));

    printf("Case #%d: %.9LE\n",t,best);
  }
  return 0;
}

