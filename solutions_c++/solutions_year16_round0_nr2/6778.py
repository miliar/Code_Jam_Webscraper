#include <iostream>
#include <map>
#include <string>

using namespace std;

int main () {
  int T;
  string S;

  cin >> T;

  for (int i = 1; i <= T; i++) {
    cin >> S;
    int count = 0;    
    int flag = 1;

    while (flag) {     
      flag = 0;

      for (int j = 0; j < S.length(); j++) {

        if (S[j] == '-') {
          flag = 1;
          int k;
          int z;
          for (k = j; k < S.length() && S[k] == '-'; k++);

          if (k < S.length()) {
            for (z = k; z < S.length() && S[z] == '+'; z++);

            if (z < S.length()) {
              z--;
              for (int w = 0; w <= z; w++) {
                S[w] = '+';
              }    
            }
            else {
              for (int w = 0; w < z; w++) {
                S[w] = '+';
              }     
            } 
          }  
          else {
            for (int w = 0; w < k; w++) {
              S[w] = '+';
            }  
          }
          
          count++;
          j = -1;
        }
        else {
          flag = 0;

          int k;
          int z;
          for (k = j; k < S.length() && S[k] == '+'; k++);

          if (k < S.length()) {
            for (z = k; z < S.length() && S[z] == '-'; z++);

            if (z < S.length()) {
              z--;
              for (int w = 0; w <= z; w++) {
                S[w] = '+';
              }    
            }
            else {
              for (int w = 0; w < z; w++) {
                S[w] = '+';
              }     
            }

            flag = 1;
            
            count += 2;
            j = -1;
          }  
          else {
            j = S.length();
          }          
          
        }

      }

    }

    cout << "Case #" << i << ": " << count << endl;

  }

  return 0;
}