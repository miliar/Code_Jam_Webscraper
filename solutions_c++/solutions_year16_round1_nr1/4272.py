
#include <iostream>
#include <string>

using namespace std;

string lastword(string word) {
  string lastword;
  lastword.push_back(word[0]);
  for(int i=1; i < word.length(); i++) {

    if ( lastword[0] <= word[i]) {
      //lastword.push_front( word[i] );
      lastword = word[i] + lastword;
    } else {
      lastword.push_back( word[i] );
    }
  }

  return lastword;
}

int main(void) {
  int T;
  cin >> T;
  string w;
  for( int i=0; i < T; i++) {
    cin >> w;
    string r = lastword( w );
    cout << "Case #" << i + 1 << ": " << r << endl;
  }
}
