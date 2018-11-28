#include <iostream>
#include <string>
#include <sstream>

using namespace std;



int main() {
  int max = 1000;
  bool square[max+1];
  bool fair[max+1];
  int squareroot[max+1];
  for(int i = 0; i < max+1; i++) {
    squareroot[i] = 0;
    square[i] = false;
    fair[i] = false;
  }
  for(int i = 1; i*i < max+1; i++) {
    square[i*i] = true;
    squareroot[i*i] = i;
  }
  for(int i = 1; i < max+1; i++) {
    string s;
    ostringstream toString;   // stream used for the conversion
    toString << i;      // insert the textual representation of 'Number' in the characters in the stream
    s = toString.str(); // set 'Result' to the contents of the stream

    bool pal = true;
    int k = 0;
    int j = s.length()-1;
    while(k <= j) {
      if(s[k] != s[j]) {
        pal = false; break;
      }
      k++;
      j--;
    }
    fair[i] = pal;
  }
  int T, s, e;
  cin >> T;
  for(int t =1 ; t<= T; t++) {
    cout << "Case #" << t << ": ";
    cin >> s >> e;
    int total = 0;
    for(int i = s; i <= e; i++) {
      if(square[i] && fair[i] && fair[squareroot[i]]) total++;
    }
    cout << total << endl;
  }
}
