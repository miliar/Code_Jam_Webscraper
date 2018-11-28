#include <iostream>
#include <string>
using namespace std;

int main (){
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t){
    string s;
    cin >> s;
    //cout << s << endl;
    
    int nbflip = 0;
    for (int i = 0; i < s.length()-1; ++i){
      if (s[i] != s[i+1])
        nbflip ++;
    }
    if (s[s.length()-1] == '-')
      nbflip ++;

    cout << "Case #" << t << ": " << nbflip << endl;
  }


}
