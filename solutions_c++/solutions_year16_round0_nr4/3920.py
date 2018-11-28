#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>

using namespace std;

int main(){
  long long T,k,c,s,pow;
  scanf("%lld",&T);

  for (long long t=1; t<=T; t++) {
    scanf("%lld",&k);
    scanf("%lld",&c);
    scanf("%lld",&s);

    printf("Case #%lld:",t);

    pow = 1;
    for (long long i=0; i+1<c; i++) {
      pow*=k;
    }

    for (long long i=0; i<k; i++) {
      printf(" %lld",pow*i+1);
    }

    putchar('\n');
  }
  return 0;
}
