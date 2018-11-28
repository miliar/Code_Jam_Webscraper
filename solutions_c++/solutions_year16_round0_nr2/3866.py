#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iostream>
#include <cmath>
#include <algorithm>

#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long ll;

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for(int o = 1; o <= T; o++){
    printf("Case #%d: ", o);
    string s;
    cin >> s;
    const int n = (int)s.size();
    vector<int> a(n);
    for(int i = 0; i < n; i++)a[i] = s[i] == '+' ? 1 : 0;
    int ans = 0;
    while(true){
      int m = (int)a.size();
      for(m--; m >= 0; m--)if(a[m] == 0)break;
      m++;
      if(m == 0)break;
      int head = a[0];
      int len = 1;
      for(; len < m; len++)if(a[len] != head)break;
      if(len == m){
        if(head == 0)ans++;
        break;
      }
      vector<int> b(m);
      if(head == 0){
        for(int i = 0; i < m; i++)b[m-i-1] = 1-a[i];
      }else{
        for(int i = 0; i < len; i++)b[i] = 0;
        for(int i = len; i < m; i++)b[i] = a[i];
      }
      a = b;
      ans++;
    }
    printf("%d\n", ans);
  }

  return 0;
}
