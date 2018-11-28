#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int cas, num, store, tmp, ans, stop;
int arr[1000];

int main() {
  scanf("%d",&cas);
  for (int k=1; k<=cas; ++k) {
    scanf("%d %d",&num, &store);
    ans=0; stop=store/2;
    for (int i=0; i<1000; ++i) arr[i]=0;
    for (int i=0; i<num; ++i) {
      scanf("%d", &tmp);
      ++arr[tmp];
    }
    for (int i=store; i>stop; --i) {
      if (arr[i]) {
        ans+=arr[i];
        tmp=arr[i];
        arr[i]=0;
        for (int j=store-i; j>=0; --j) {
          if (arr[j]>=tmp) {arr[j]-=tmp; tmp=0; break;}
          else {tmp-=arr[j]; arr[j]=0;}
        }
      }
    }
    stop=0;
    for (int i=0; i<=store; ++i) stop+=arr[i];
    ans+=(stop+1)/2;
    

    printf("Case #%d: %d\n",k,ans);
  }
  return 0;
}
