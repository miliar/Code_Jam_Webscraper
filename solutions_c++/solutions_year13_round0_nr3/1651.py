#include <stdio.h>
#include <string.h>
#include <math.h>

char str[20];
long long A[10000010];

bool isPalid(long long x) {
  int len = 0;
  while(x > 0) {
    str[len++] = x%10;
    x /= 10;
  }
  for(int i=0;i<len;++i)
    if(str[i] != str[len-i-1])
      return false;
  return true;
}

void Build() {
  for(long long i=1;i<=10000000;++i)
    if( isPalid(i) && isPalid(i*i) )
      A[i] = 1;
  for(int i=1;i<=10000000;++i)
    A[i] += A[i-1];
}

int main() {
  Build();

  int t, kas=0;
  scanf("%d",&t);
  while(t--) {
    long long a, b, pa;
    scanf("%lld%lld",&a,&b);
    pa = a;
    a = (long long)sqrt(a);
    b = (long long)sqrt(b);
    if(a * a  == pa)  --a;
    printf("Case #%d: %lld\n", ++kas, A[b]-A[a]);
  }

  return 0;
}

