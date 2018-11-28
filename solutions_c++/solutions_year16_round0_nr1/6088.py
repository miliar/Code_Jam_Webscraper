#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <set>

using namespace std;

int main(){
  vector<int> num, seen;
  int n, k, T, seen_num = 0;
  int res;

  seen.resize(10,0);

  scanf("%d",&T);

  for (int t=1; t<=T; t++) {
    seen_num = 0;
    for (int i=0; i<10; i++) {
      seen[i]=0;
    }
    res = 0;

    scanf("%d",&n);

    if (n==0) {
      printf("Case #%d: INSOMNIA\n",t);
      continue;
    }

    for (int i=1; res == 0; i++) {
      k = n*i;
      num.clear();
      while (k!=0) {
        num.push_back(k%10);
        k/=10;
      }
      for (int j=0; j<num.size(); j++) {
        if (seen[num[j]] == 0) {
          seen[num[j]] = 1;
          seen_num++;
          if (seen_num == 10) {
            res = n*i;
            break;
          }
        }
      }
    }

    printf("Case #%d: %d\n",t,res);
  }

  return 0;
}
