#include <iostream>
#include <vector>

using namespace std;

int main () {
  int T, N, M, tmp;
  vector < vector<int> > lawn;
  // Vector of vertical maximums (max in the given column).
  vector <int> vertical;
  // Vector of horizontal maximums (max in the given row).
  vector <int> horizontal;
  
  cin >> T;
  
  for (int t = 0; t < T; ++t) {
    cin >> N >> M;
    
    lawn.resize(N);
    vertical = vector<int>(N, 0);
    horizontal = vector<int>(M, 0);
    
    for (int i = 0; i < N; ++i) {

      lawn[i].resize(M);
      
      for (int j = 0; j < M; ++j) {
	cin >> lawn[i][j];
	if (lawn[i][j] > vertical[i]) {
	  vertical[i] = lawn[i][j];
	}
	if (lawn[i][j] > horizontal[j]) {
	  horizontal[j] = lawn[i][j];
	}
      }
      
    }
    
    bool isPossible = true;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < M; ++j) {
	if ((lawn[i][j] < vertical[i]) && (lawn[i][j] < horizontal[j])) {
	  isPossible = false;
	  break;
	}
      }
    }
    
    string answer;
    
    if (isPossible)
      answer = "YES";
    else
      answer = "NO";
    
    cout << "Case #" << t + 1 << ": " << answer << endl;
  }
  
}