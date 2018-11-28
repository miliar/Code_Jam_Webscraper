#include <iostream>
#include <cstring>
using namespace std;
int main() {
  int T, len, cnt;
  char str[106];
  cin >> T;
    for (int i = 0; i < T; ++i) {
      cnt = 0;
      cin >> str;
      len = strlen(str);
      for(int j = 0; j < len-1; j++) {
        if(str[j] == str[j+1]) 
          continue;
        else 
          cnt++;
      }
      if(str[len-1] == '-') cnt++;
      cout << "Case #" << i+1 << ": " << cnt << endl;         
    }
  return 0;
}
