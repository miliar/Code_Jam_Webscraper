#include<cstdio>
#include<vector>
using namespace std;

int main() {
  int Z;
  scanf("%d", &Z);

  for(int z=1; z<=Z; z++) {
    int n;
    scanf("%d", &n);
    printf("Case #%d: ", z);

    if(!n) {
      printf("INSOMNIA\n");
      continue;
    }

    vector<bool> spotted(10, false);
    int digits_spotted = 0;

    long long i;

    for(i=n; digits_spotted<10; i+=n) {
      long long x = i;

      while(x>0) {
        int r = x%10;
        if(!spotted[r]) {
          digits_spotted++;
          spotted[r] = true;
        }
        x/=10;
      }

    }
    printf("%lld\n", i-n);
  }

return 0;
}
