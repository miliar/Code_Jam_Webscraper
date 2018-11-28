#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>

using namespace std;

int T;

long long cntSheep(long long n){
  if(n == 0) return -1;
  set<long long> t;
  long long cur = 0;
  for(int i = 0;  i < 10; i++) t.insert(i);
  while(1){
    cur += n;
    long long tmp = cur;
    while(tmp){
      t.erase(tmp % 10);
      if(t.size() == 0) return cur;
      tmp = tmp / 10;
    }
  }
}

int main(int argc, char * argv []){
  scanf("%d", &T);
  for(int i = 0; i < T; i++){
    int N;
    long long ANS;
    scanf("%d", &N);
    
    printf("Case #%d: ", i + 1);
    if((ANS = cntSheep(N)) < 0) printf("INSOMNIA\n");
    else printf("%lld\n", ANS);
  }
  return 0; }


