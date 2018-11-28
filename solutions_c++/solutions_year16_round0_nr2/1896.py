#include <iostream>
#include <cassert>

using namespace std;

#define MAXN 105

int main(){
  int T;
  string s;
  
  cin >> T;
  
  for(int tc = 1;tc <= T;++tc){
    cin >> s;
    
    int N = s.size(),ans = 0;
    
    for(int i = 0;i < N;){
      int e = i;
      
      while(e < N && s[e] == s[i]) ++e;
      
      ++ans;
      i = e;
    }
    
    if(s[N - 1] == '+') --ans;
    
    cout << "Case #" << tc << ": " << ans << '\n';
  }
  
  return 0;
}
