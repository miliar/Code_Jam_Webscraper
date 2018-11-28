#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;



int L, X;
int LX;
string str;

int charat(int i) {
  return str[i % L] - 105;
}

#define I 0
#define J 1
#define K 2
#define P1 3
#define MI 4
#define MJ 5
#define MK 6
#define M1 7

// transitions   I    J   K 
int trans[8][3] = { {M1,  K, MJ},
                {MK, M1,  I},
                { J, MI, M1},
                { I,  J,  K},
                {P1, MK,  J},
                { K, P1, MI},
                {MJ,  I, P1},
                {MI, MJ, MK} };

int main() {
  int cases;
  cin >> cases;
  
  vector<string> answer { "NO", "YES" };
  for (int c = 1; c <= cases; c++) {
    cin >> L >> X >> str;
    LX = L*X;

    bool found {false};
    if (LX > 2) {
      int state = P1;
      // test if possible
      for (int i = 0; i < LX; i++)
        state = trans[state][charat(i)];

      if (state == M1) {
        state = P1;
        for (int i = 0; i < LX; i++) {
          state = trans[state][charat(i)];
          if (state == I) {
            state = P1;

            // test if possible
            for (int j = i+1; j < LX; j++)
              state = trans[state][charat(j)];

            if (state != I)
              break;
    
            state = P1;
            for (int j = i+1; j < LX; j++) {
              state = trans[state][charat(j)];
              if (state == J) {
                state = P1;
                for (int k = j+1; k < LX; k++) {
                  state = trans[state][charat(k)];
                }
                if (state == K)
                  found = true;
                state = J;
              }
            }
            if (found)
              break;
            state = I;
          }
        }
      }
    }
    cout << "Case #" << c << ": " << answer[found] << endl;
  }
}
