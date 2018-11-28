# include <iostream>
# include <string>
# include <cstdlib>
# include <string.h>


using namespace std;

int main() {
  int T,times;
  cin >> T;
  for ( int i = 1 ; i <= T ; i++ ){
    times = 0;
    string s;
    cin >> s;
    char str[s.size()];
    strcpy(str, s.c_str());
    while ( 1 ) {
      bool all_small = false;
      for ( int j = 0 ; j < s.size() ; j++ ) {
        if ( str[j] == '+') all_small = true;
        else {
          all_small = false;
          break;
        }
      }
      if ( all_small )break;
      if ( str[0] == '+') {
        str[0] = '-';
        for ( int j = 1 ; j < s.size() ; j++){
          if ( str[j] == '-'){
            break;
          }
          else {
            str[j] = '-';
          }
        }
      }
      else {
        str[0] = '+';
        for ( int j = 1 ; j < s.size() ; j++){
          if ( str[j] == '+'){
            break;
          }
          else {
            str[j] = '+';
          }
        }
      }
      times++;
    }
    cout << "Case #" << i << ": " << times << endl;
  }
  return 0;
} // main()
