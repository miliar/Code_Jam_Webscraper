#include <stdio.h>

long long N, prize, player;

long long best(){
  long long minnow = N+1;
  long long tnum = player-1;
  long long dec = 1;
  while(tnum >= player-prize){
    tnum -= dec;
    dec *=2;
    minnow--;
  }
  /*
  for(int i=player-1; i>=player-prize; i--){
    itemp = findone(i);
    if(itemp < minnow) minnow = itemp;
  }
  */
  //printf("minnow = %d\n", minnow);
  
  long long canLose = N-minnow;
  long long ans = 1LL<<(minnow);
  
  return player - ans;
}

long long worst(){
  long long hiRank = player - prize;
  long long tp = player;
  long long ctLose=0;
  while(hiRank < tp){
    tp/=2;
    ctLose++;
  }
  //printf("ctLose =%d\n", ctLose);
  long long willLose = (1LL<<ctLose) - 1;
  long long ans = willLose-1;
  if(ans < 0) ans = 0;
  if(ans > player-1) ans = player-1;
  return ans;
}

int main(){
  int jcase;
  
  //freopen("B-small-attempt0.in", "r", stdin);
  //freopen("B-small-attempt0.out", "w", stdout);
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  
  scanf("%d", &jcase);
  for(int icase=0; icase<jcase; icase++){
    scanf("%lld %lld", &N, &prize);
    player = 1LL<<N;
    printf("Case #%d: %lld %lld\n", icase+1, worst(), best());
  }
  return 0;
}
