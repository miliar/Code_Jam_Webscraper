#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {

  if(argc != 2) {
    cout << "please pass exactly one argument" << endl;
    exit(1);
  }
  ifstream input;
  input.open(argv[1]);
  int t(0);

  input >> t;
  for(int i(0); i != t; ++i) {
      cout << "Case #" << i+1 << ": ";
      int n(0);
      int m(0);
      input >> n >> m;
      vector<vector<int> > lawn(n, vector<int>(m,0));
      vector<int> max_in_row(n,0);
      vector<int> max_in_col(m,0);
      for(int j(0); j != n; ++j) {
          for(int k(0); k != m; ++k) {
              int height;
              input >> height;
              lawn[j][k] = height;
              max_in_row[j] = max(max_in_row[j], height);
          }
      }
      for(int k(0); k != m; ++k) {
          for(int j(0); j != n; ++j) {
              max_in_col[k] = max(max_in_col[k], lawn[j][k]);
          }
      }
      bool possible(true);
      for(int j(0); j != n; ++j) {
          for(int k(0); k != m; ++k) {
              if(lawn[j][k] != max_in_col[k] && lawn[j][k] != max_in_row[j]) {
                  possible = false;
                  break;
              }
          }
          if(!possible) break;
      }
      if(possible) cout << "YES" << endl;
      else cout << "NO" << endl;



  }

  input.close();
  return 0;
}
