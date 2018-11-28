#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <deque>
#include <string>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <time.h>
#include <bitset>
#include <list>
#include <assert.h>
#include <time.h>
using namespace std;

int main () {
  int T;
  cin >> T;

  int N, P, R, S;

  int target;
  string word;
  string result;

  for(int x = 0; x < T; ++x) {
    cin >> N;
    cin >> R;
    cin >> P;
    cin >> S;

    int Y = pow(2,N);
    int Z = Y / 3;

    word = "";
    result = "";
    bool logic = true;

    if(P != Z && P != (Z+1)) {
      logic = false;
    }

    if(R != Z && R != (Z+1)) {
      logic = false;
    }

    if(S != Z && S != (Z+1)) {
      logic = false;
    }

    if(logic) {
      if(N % 2 == 0) {
        if(P == Z+1) {
          target = 0;
        } else
        if(R == Z+1) {
          target = 1;
        } else
        if(S == Z+1) {
          target = 2;
        }
      } else {
        if(P == Z) {
          target = 0;
        } else
        if(R == Z) {
          target = 1;
        } else
        if(S == Z) {
          target = 2;
        }    
      }

      target = (target + N)%3;

      if(target == 0) {
        word = "P";
      } else
      if(target == 1) {
        word = "R";
      } else
      if(target == 2) {
        word = "S";
      }

      int size = 1;

      for(int i = 0; i < N-2; ++i) {
        size = word.size();
        for(int j = 0; j < size; ++j) {
          if(word.substr(j,1) == "P") {
            result += "PR";
          } else
          if(word.substr(j,1) == "R") {
            result += "SR";
          } else
          if(word.substr(j,1) == "S") {
            result += "SP";
          }       
        }
        word = result;
        result = "";
      }

      if(N > 1) {
        size = word.size();
        for(int j = 0; j < size; ++j) {
          if(word.substr(j,1) == "P") {
            result += "PR";
          } else
          if(word.substr(j,1) == "R") {
            result += "SR";
          } else
          if(word.substr(j,1) == "S") {
            result += "PS";
          }       
        }
        word = result;
        result = "";
      }

      size = word.size();
      for(int j = 0; j < size; ++j) {
        if(word.substr(j,1) == "P") {
          result += "PR";
        } else
        if(word.substr(j,1) == "R") {
          result += "RS";
        } else
        if(word.substr(j,1) == "S") {
          result += "PS";
        }       
      }
    } else {
      result = "IMPOSSIBLE";
    }

    cout << "Case #" << x+1 << ": " << result << endl;
  }

  return 0;
}