# include <cstdio>

long long bestrank(long long pos,long long N)
{
  long long goodpos=0,rank=0,add=(1ll<<(N-1)),addcnt=2;
  while(1)
  {
    if(pos<=goodpos)return rank;
    rank+=add;
    goodpos+=addcnt;
    add>>=1;
    addcnt<<=1;
  }
}

long long worstrank(long long pos,long long N)
{
  long long goodpos=0,rank=0,add=1,addcnt=(1ll<<(N-1));
  while(1)
  {
    if(pos<=goodpos)return rank;
    rank+=add;
    goodpos+=addcnt;
    add<<=1;
    addcnt>>=1;
  }
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    long long N,P;
    scanf("%Ld %Ld",&N,&P);

    long long start,mid,end;
    long long lucky,unlucky;

    start=0;end=(1ll<<N);
    while(end-start>1)
    {
      mid=(start+end)>>1;
      if(bestrank(mid,N)<P)start=mid;
      else end=mid;
    }
    lucky=start;

    start=0;end=(1ll<<N);
    while(end-start>1)
    {
      mid=(start+end)>>1;
      if(worstrank(mid,N)<P)start=mid;
      else end=mid;
    }
    unlucky=start;

    printf("Case #%d: %Ld %Ld\n",t,lucky,unlucky);
  }
  return 0;
}
