#include <iostream>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int i=0;i<t;i++){
    string s;
    cin >> s;
    cout << "Case #" << i+1 << ": ";
    bool end = false;
    int count = 0;
    while(!end){
      int len = 1;
      char c = s[0];
      bool flag=true;
      int start = 0;
      for(int i=0;i<(int)s.size();i++){
        if(flag && s[i] == '+')
          start++;
        if(s[i] != '+')
          flag = false;
      }
      flag = true;
      for(int i=start+1;i<(int)s.size();i++){
        if(flag && s[i] == '-')
          len++;
        if(s[i] != '-')
          flag = false;
      }
      if(start == (int)s.size() && c == '+'){
        cout << count << endl;
        end = true;
      }
      count++;
      if(c == '-'){
        for(int i=0;i<len;i++)
          s[i] = '+';
      }else{
        for(int i=0;i<start;i++)
          s[i] = '-';
        for(int i=0;i<len;i++)
          s[start+i] = '+';
      }
    }
  }
  return 0;
}
