#include<cstdio>
#include<cmath>
#include<vector>
using namespace std;
int main() {
  int n; scanf("%d", &n);
  vector<int> digits;
  digits.reserve(150);
  for(int i=1;i<=n;i++) {
    long long a,b;scanf("%lld%lld",&a,&b);
    long long cc=0;
    for(long long j=a;j<=b;j++) {
      long long sq = (long long)sqrt(j);
      if (sq * sq == j) {
        long long n = j;
        while(n!=0) {
          digits.push_back(n%10);
          n = n/10;
        }
        int ff=true;
        for (unsigned int k=0;k<digits.size()/2+1;k++)
          if (digits[k]!=digits[digits.size()-1-k]) {
            ff=false;break;
          }
        if (ff) { 
          digits.clear();
        long long n = sq;
        while(n!=0) {
          digits.push_back(n%10);
          n = n/10;
        }
          for (unsigned int k=0;k<digits.size()/2+1;k++)
            if (digits[k]!=digits[digits.size()-1-k]) {
              ff=false;break;
            }
          if(ff) cc++;
        }
      }
      digits.clear();
    }
    printf("Case #%d: %lld\n",i,cc);
  }
	return 0;
}
