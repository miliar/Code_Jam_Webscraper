#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;

int n;
int a[2048];
bool ok(int m){
  int cur = m;
  for(int i = 0; i < n; i++){
    if(cur < i)return false;
    cur += a[i];
  }
  return true;
}

int main(int argc, char* argv[]){
  int T;
  scanf("%d", &T);
  char s[2048];
  for(int o = 1; o <= T; o++){
    scanf("%d", &n);
    n++;
    scanf("%s", s);
    for(int i = 0; i < n; i++)
      a[i] = s[i] - '0';
    int left = 0, right = n*2;
    int ans = n;
    while(left <= right){
      int m = (left+right)/2;
      if(ok(m)){
        ans = min(ans, m);
        right = m-1;
      }else{
        left = m+1;
      }
    }
    printf("Case #%d: %d\n", o, ans);
  }

  return 0;
}

