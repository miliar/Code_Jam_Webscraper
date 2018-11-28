#include <iostream>
#include <map>
#include <string>

using namespace std;

int main () {
  int T;
  map<char, int> m;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    int flag = 1;
    int counter = 0;
    int v;
    cin >> v;
    string N;

    while (flag) {      
      counter++;    

      N = to_string(v * counter);

      if (N == "0") {
        cout << "Case #" << i << ": INSOMNIA" << endl;
        flag = 0;
      }
      else {
      
        for (int j = 0; j < N.length(); j++) {
            m[ N[ j ] ] = 1;        
        }

        flag = 0;
        for (char j = '0'; j <= '9'; j++)        
          if (m[j] == 0) {
            flag = 1;
            break;
          }

        if (!flag) {
            cout << "Case #" << i << ": " << N << endl;
        }

      }
    }    

    m.clear();
  }
  return 0;
}