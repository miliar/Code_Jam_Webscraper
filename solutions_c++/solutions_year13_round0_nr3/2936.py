// Problem C. Fair and Square   , not fit in Second Large input (10^100)
// Contest: Google CodeJam Qualification Round 2013
// Author: LotK

#include <cstdio>
#include <cstring>
#include <cstdlib>

int data[10000000];

int checkPalindrome(long long x) {
  char buffer[20];
  itoa(x, buffer, 10);
  int len = strlen(buffer);
  long long i;
  for(i=0 ; i<len/2 ; i++) {
    if(buffer[i] != buffer[len-1-i]) break;
  }
  if(i<len/2) return 0;

  itoa(x*x, buffer, 10);
  len = strlen(buffer);
  for(i=0 ; i<len/2 ; i++) {
    if(buffer[i] != buffer[len-1-i]) break;
  }
  if(i<len/2) return 0;

  return 1;
}

long long sol(long long x) {
  long long left=1, right=10000000, mid;
  while(left<=right) {
    mid = (left+right)/2;
    if(mid*mid <= x && (mid+1)*(mid+1) > x) return mid;
    else if(mid*mid<x) left = mid+1;
    else right = mid-1;
  }
}

int main() {
  int t, tt, i;
  long long a, b, tmpa, tmpb;
  scanf("%d", &tt);
  data[0]=0;
  for(i=1 ; i<10000000 ; i++) {
    if(checkPalindrome(i)) data[i] = data[i-1]+1;
    else data[i]=data[i-1];
  }
   //for(i=0 ; i<1000; i++) if(data[i]!=data[i-1] )printf("%d %d %d\n", i, i*i, data[i]);
  for(t=0; t<tt ; t++) {
    scanf("%lld%lld", &a, &b);
    tmpb=sol(b);
    tmpa=sol(a);
    if(tmpa*tmpa == a) tmpa-=1;
    int ans = data[tmpb] - data[tmpa];
    printf("Case #%d: ", t+1);
    printf("%d\n", ans);
  }
}
