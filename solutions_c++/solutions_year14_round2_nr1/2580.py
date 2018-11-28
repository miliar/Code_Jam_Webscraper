#include <iostream>
#include <sstream>
#include <string> 
#include <cmath>

using namespace std;

void case_(int n, string& answer) {
  cout.precision(7);
  cout << "Case #" << n << ":" << " " << fixed << answer << endl; 
}


void toString(int number, string& result) {  
  ostringstream convert;
  convert << number;    
  result = convert.str();  
}

void minimumString(string& str, string& minimum, int rep[100]) {
  char curr = str.at(0);
  minimum += curr;
  int step = 0;
  rep[0] = 0;
  for (int i = 0; i < str.length(); i++) {
    if (str.at(i) != curr) {
      curr = str.at(i);
      minimum += curr;
      step++;
      rep[step] = 1;
    } else {
      rep[step]++;
    }
  }
}

int dist(int rep1[100], int rep2[100]) {
  int d = 0;
  for (int i = 0; i < 100; i++) {
    d += abs(rep1[i]-rep2[i]);
  }
  return d;
}

void doCase(int n) {
  int N;
  int minMoves = 0;
  string fegla = "Fegla Won";
  cin >> N;
  string str[N];
  int rep[100][100] = {0};
  string minimum;
  cin >> str[0];
  minimumString(str[0], minimum, rep[0]);
  for (int i = 1; i < N; i++) {
    cin >> str[i];
    string newMin;
    minimumString(str[i], newMin, rep[i]);
    if (newMin != minimum) {
      case_(n, fegla);
      return;
    } 
  }

  for (int i = 0; i < 100; i++) {
    int minpartial = 0;    
    for (int j = 0; j < N; j++) {
      int partial = 0;
      for (int k = 0; k < N; k++) {
        partial += abs(rep[j][i] - rep[k][i]);
      }
      if (minpartial > partial || j == 0) {
        minpartial = partial;
      }
    }
    minMoves += minpartial;
  } 
  string result;
  toString(minMoves, result);
  case_(n, result);
}

int main() {
  int cases;
  cin >> cases;
  for (int i = 0; i < cases; i++) {
    doCase(i+1);
  }
}
