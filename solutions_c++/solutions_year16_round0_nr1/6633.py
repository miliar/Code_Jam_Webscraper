# include <iostream>
# include <cstdlib>
# include <string>
# include <sstream>

using namespace std;

int main() {
  int T, n, c;
  cin >> T;
  for ( int i = 1 ; i <= T ; i++ ) {
    char digets[] = { '0' , '1' , '2' , '3' , '4' , '5', '6', '7', '8', '9'};
    cin >> n;
    if ( n == 0 ) {
      cout << "Case #" << i << ": INSOMNIA" << endl;
      continue;
    }
    c = n;
    bool end = false;
    while ( 1 ) {
      stringstream strs;
      strs << n;
      string str = strs.str();
      char const *pchar = str.c_str();
      for ( int z = 0 ; z < str.size() ; z++) {
        digets[pchar[z] - '0'] = ' ';
      }
      for ( int j = 0 ; j < 10 ; j++ ){
        if ( digets[j] == ' ')end = true;
        else {
          end = false;
          break;
        }
      }
      if ( end )break;
      n += c ;
    }
    cout << "Case #"<< i << ": " << n << endl;
  }

  return 0;
} // main()
