#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>

using namespace std;

int main(){
  vector<long long> num;
  vector<bool> sito;
  vector<long long> primes;
  vector<long long> res;
  long long val;

  //printf("memory not yet allocated\n");

  sito.resize(10e6,0);

  printf("Case #1:\n");
  //printf("memory allocated\n");

  for (long long i=2; i<sito.size(); i++) {
    //printf("Processing: %lld\n",i);
    if (!sito[i]) {
      primes.push_back(i);
      for (long long j=2*i; j<sito.size(); j+=i) {
        sito[j] = 1;
      }
    }
  }

  /*for (long long i=0; i<primes.size(); i++) {
    printf("%lld\n",primes[i]);
  }*/

  long long n=16;
  long long needed=50;

  num.resize(n,0);
  num[0] = num[n-1] = 1;

  for (long long o = 0; o<needed;) {
    for (long long i=n-2; i>0 ;i--) {
      if (num[i] == 0) {
        num[i] = 1;
        break;
      } else {
        num[i] = 0;
      }
    }

    /*printf("Trying: ");
    for (long long i=0; i<n; i++) {
      printf("%lld",num[i]);
    }putchar('\n');*/

    res.clear();

    for (long long base = 2; base <=10; base++) {
      val = 0;
      for (long long i=0; i<n; i++) {
        val*=base;
        val+=num[i];
      }

      //printf("base %lld %lld\n",base,val);

      for (long long i=0; i<primes.size(); i++) {
        if (val%primes[i] == 0 && val != primes[i]) {
          //printf("div by: %d\n", primes[i]);
          res.push_back(primes[i]);
          break;
        }
      }
    }

    if (res.size() == 9) {
      o++;
      for (long long i=0; i<n; i++) {
        printf("%lld",num[i]);
      }
      for (long long i=0; i<res.size(); i++) {
        printf(" %lld",res[i]);
      }putchar('\n');
    }
  }

  //scanf("%lld",&n);

  //printf("%lld\n",k);

  return 0;
}
