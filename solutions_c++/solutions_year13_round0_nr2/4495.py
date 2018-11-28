#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool all_eq(vector<vector<int> >& matrix, int r, int c, int N, int M, string param) {
  //cout << "checking elem at " << r << " " << c << endl;
  if ("r" == param) {
    for (int j = 0; j < M; ++j) {
      if (matrix[r][j] != matrix[r][c]) {
        //cout << "row " << r << " isn't all " << matrix[r][c] << endl;
        return false;
      }
    }
  } else {
    for (int i = 0; i < N; ++i) {
      if (matrix[i][c] != matrix[r][c]) {
      	//cout << "column " << c << " isn't all " << matrix[r][c] << endl;
        return false;
      }
    }
  }
  return true;
}

bool solve(vector<vector<int> >& matrix, int N, int M) {
  int lowest = matrix[0][0];
  int highest = matrix[0][0];
  
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < M; ++j) {
      lowest = min(lowest, matrix[i][j]);
      highest = max(highest, matrix[i][j]);
    }
  }
  //cout << "lowest=" << lowest << " ";
  //cout << "highest=" << highest << endl;
  while (lowest < highest) {
    for (int i = 0; i < N; ++i) {
    	for (int j = 0; j < M; ++j) {
    	  if (matrix[i][j] == lowest) {
    	    bool rowtest = all_eq(matrix, i, j, N, M, "r");
    	    bool coltest = all_eq(matrix, i, j, N, M, "c");
    	    if (!(rowtest || coltest)) return false;
    	  }
    	}
    }
    for (int i = 0; i < N; ++i) {
    	for (int j = 0; j < M; ++j) {
    	  if (matrix[i][j] == lowest) {
    	    ++matrix[i][j];
    	  }
    	}
    }
    ++lowest;
  }
  
  return true;
}

int main(int argc, char *argv[]) {
  int n_cases;
  
  cin >> n_cases;
  
  for (int t = 0; t < n_cases; ++t) {
    int N, M;
    cin >> N >> M;
    vector<vector<int> > matrix(N, vector<int>(M, 0));
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
        cin >> matrix[i][j];
      }
    }
    
    bool res = solve(matrix, N, M);
    cout << "Case #" << t + 1 << ": ";
    if (res) {
      cout << "YES";
    } else {
      cout << "NO";
    }
    cout << endl;
  }
  return 0;
}

