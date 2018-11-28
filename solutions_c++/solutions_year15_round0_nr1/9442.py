#include <bits/stdc++.h>

using namespace std;

char in[1010];

int main() {
  int T; scanf("%d", &T);
  
  for(int t = 0; t < T; t++) {
    int k; scanf("%d", &k);
    
    int cnt = 0, ans = 0;
    
    for(int i = 0; i <= k; i++) {
      scanf(" %c", &in[i]);

      int l;
      
      if(in[i] == '0')
	l = 0;
      else if(in[i] == '1')
	l = 1;
      else if(in[i] == '2')
	l = 2;
      else if(in[i] == '3')
	l = 3;
      else if(in[i] == '4')
	l = 4;
      else if(in[i] == '5')
	l = 5;
      else if(in[i] == '6')
	l = 6;
      else if(in[i] == '7')
	l = 7;
      else if(in[i] == '8')
	l = 8;
      else
	l = 9;
      
      if(cnt < i) {
	ans += (i - cnt);
	cnt += (i - cnt);
      }
      
      cnt += l;
    }
    
    printf("Case #%d: %d\n", t + 1, ans);
  }
  
  return 0;
}
