#include <iostream>
using namespace std;

char s[100];
unsigned len;

char flip(char x) {
  return (x == '+') ? '-' : '+';
}

void turn(char *x, int j) {
  for (int k = 0; k <= j/2; k++) {
    char a = x[k];
    char b = x[j - k];
    x[k] = flip(b);
    x[j-k] = flip(a);
  }
}

void print() {
  unsigned len = (unsigned)strlen(s);
  for (int i = 0; i < len; i++) {
    cout << s[i] ;
  }
  cout << endl;
}

int pancakes(char *x, int j, int flipped) {
  if (j < 0)
    return flipped;
  
  if (x[j] == '+')
    return pancakes(x, j-1, flipped);
  
  //print();

  //cout << "s[" << j << "] = " << s[j] << endl;
  if (x[0] == '-') {
    turn(x, j);
    return pancakes(x, j-1, flipped + 1);
  } else {
    int f = 0;
    int min = INT_MAX;
    int minK = -1;
    for (int k = 0; k < j; k++) {
      //cout << "K= " << k << ", J= " << j << endl;
      if (x[k] == '-')
        continue;
      char aux[100];
      for (int p=0; p<len; p++) aux[p] = x[p];
      turn(aux, k);
      turn(aux, j);
      f = pancakes(aux, j-1, flipped + 2);
      if (f < min) {
        min = f;
        minK = k;
      }
    }
    if (minK != -1) {
      turn(x, minK);
      //print();
      turn(x, j);
      return min;
    } else 
      return 0;
  }
}

int main() {
    int t;
    cin >> t; 

    for (int i = 1; i <= t; ++i) {
      cin >> s; 
      len = (unsigned)strlen(s);
      //cout << s << endl;
      int turns = pancakes(s, len-1, 0);
      //print();
      cout << "Case #" << i << ": " << turns << endl;
      
    }
    return 0;
}
