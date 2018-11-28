#include <iostream>
using namespace std;

#define DIM 100

class Lawn {
  int n, m;
  int lawn[DIM][DIM];
  bool squareImpossible(int x, int y);
public:
  Lawn ();
  bool Impossible();
  string verdict();
  void print();
};

Lawn::Lawn() {
  string line;
  scanf("%d %d\n", &n, &m);
  
  for (int i = 0; i < n; i++) {
    getline(cin, line);
    for (int j = 0; j < m; j++) {
      lawn[i][j] = line[2*j] - '0';
    }
  }
};

bool Lawn::squareImpossible(int x, int y) {
  // Square is impossible if there is a number that is larger than it
  // in both the row and column
  int val = lawn[x][y];

  // check row first
  bool numLargerInRow = false;
  for (int j = 0; j < m; j++) {
    if (lawn[x][j] > val) numLargerInRow = true;
  }
  // then check col
  bool numLargerInCol = false;
  for (int i = 0; i < n; i++) {
    if (lawn[i][y] > val) numLargerInCol = true;
  }
  return numLargerInRow && numLargerInCol;
}

bool Lawn::Impossible() {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (this->squareImpossible(i,j)) return true;
    }
  }
  return false;
}

string Lawn::verdict() {
  if (this->Impossible()) return "NO";
  return "YES";
}

void Lawn::print() {
  cout << "Lawn dimensions: " << n << "x" << m << "\n";
  cout << "Verdict: " << this->verdict() << "\n";
  cout << "Lawn:\n";
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cout << lawn[i][j];
    }
    cout << "\n";
  }
};

void oneLawn(int n) {
  Lawn *l = new Lawn();
  cout << "Case #" << n << ": " << l->verdict() << "\n";
}

int main() {
  int numTests; 
  string empty;
  cin >> numTests; getline(cin, empty);
  for (int n = 0; n < numTests; n++) {
    oneLawn(n+1);
  }

}
