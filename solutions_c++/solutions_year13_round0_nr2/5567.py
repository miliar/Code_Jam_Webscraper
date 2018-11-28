#include <iostream>

using namespace std;

int** lawn;

void print(int n, int m) {
  cout << n << ' ' << m << '\n';
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      cout << lawn[i][j] << ' ';
    }
    cout << '\n';
  }
}

/* Print YES or NO*/
void checkLawn(int n, int m) {
  bool  left = false,
        up = false,
        right = false,
        down = false;
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      left = false; up = false;
      right = false; down =false;
      int current = lawn[i][j];
      // left
      for(int k = 0; k < j; ++k) {
        if(lawn[i][k] > current) {
          left = true;
          break;
        }
      }

      for(int k = j + 1; k < m; ++k) {
        if(lawn[i][k] > current) {
          right = true;
          break;
        }
      }

      for(int k = 0; k < i; ++k) {
        if(lawn[k][j] > current) {
          up = true;
          break;
        }
      }

      for(int k = i+1; k < n; ++k) {
        if(lawn[k][j] > current) {
          down = true;
          break;
        }
      }

      if((left || right) && (up || down)) {
        cout << "NO";
        return;
      }
    }
  }
  cout << "YES";
}

void makeTest(int number) {
  int n, m;

  cin >> n;
  cin >> m;

  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < m; ++j) {
      cin >> lawn[i][j];
    }
  }

  cout << "Case #" << number << ": ";
  checkLawn(n,m);
  cout << '\n';
}

int main(int argc, char* argv[]) {
  ios::sync_with_stdio(false);

  int number_of_tests;
  cin >> number_of_tests;

  lawn = (int**)new int[100];

  for(int i = 0; i < 100; ++i){
    lawn[i] = new int[100];
  }

  for(int i = 1; i <= number_of_tests; ++i) {
    makeTest(i);
  }

  for(int i = 0; i < 100; ++i){
    delete[] lawn[i];
  }
  delete[] lawn;

  return 0;
}