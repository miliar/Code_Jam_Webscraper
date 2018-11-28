#include <cstdio>
#include <iostream>

using namespace std;


int f(){

  int sum = 0;
  int add = 0;
  char s[1005];
  int S;
  int i;
  char j;
  scanf("%d", &S);
  scanf("%s", s);

  for(i=0;i<=S;i++) {
    if (sum >= i) {
      sum += (s[i]-'0');
    } else {
      int z = i - sum;
      add += z;
      sum += z + (s[i]-'0');
    }
  }

  return add;
}

int main() {
  int i,n;
  scanf("%d", &n);
  for(i=1;i<=n;i++){
    printf("Case #%d: %d\n", i, f());
  }
}