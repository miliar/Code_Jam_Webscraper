#include <bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin >> T;
  
  for(int tc = 1 ; tc <= T ; tc++){
    int smax;
    string s;
    cin >> smax >> s;
    
    int ans = 0;    
    int standing = 0;
    standing += s[0] - '0';
    
    for(int i = 1 ; i < (int)s.size() ; i++){
      if(standing < i){
	int n = i - standing;
	ans += n;
	standing += n;
      }
      standing += s[i] - '0';      
    }
    
    printf("Case #%d: %d\n", tc, ans);
  }
  
  
  return 0;
}
