
#include<iostream>
#include<sstream>
#include<string>
#include<map>
#include<vector>
#include<set>


int check_row(int row, int col, int N, int M, int **table, int h) {
  int found = 0;
  for (int i=0;i<M; i++) {
    if (table[row][i] == h) {
      found++;
    } else if (table[row][i] != -1) {
      return -1;
    }
  }
  return found;
}

void mark_row(int row, int col, int N, int M, int **table, int h) {
  for (int i=0;i<M; i++) {
    if (table[row][i] == h) {
      table[row][i] = -1;
    }
  }
}

int check_col(int row, int col, int N, int M, int **table, int h) {
  int found = 0;
  for (int i=0;i<N; i++) {
    if (table[i][col] == h) {
      found++;
    } else if (table[i][col] != -1) {
      return -1;
    }
  }
  return found;
}

void mark_col(int row, int col, int N, int M, int **table, int h) {
  for (int i=0;i<N; i++) {
    if (table[i][col] == h) {
      table[i][col] = -1;
    }
  }
}


int main() 
{
  using namespace std;

  int T = 0;
  cin >> T;

  std::string str;
  getline(cin, str);

  int i = 0;
  for (i=1;i<=T;i++) 
  {
    bool ans = true;
    int N,M;

    cin >> N;
    cin >> M;
    int **table = new int*[N];

    // Read lawn
    set<int> grass_h;
    multiset<int> grass_count;
    for (int row=0; row<N; row++) {
      table[row] = new int[M];

      for (int col=0; col<M; col++) {
        cin >> table[row][col] ; // read height
        grass_h.insert(table[row][col]);
        grass_count.insert(table[row][col]);
      }
    }

    bool stop = false;
    for (set<int>::iterator itr = grass_h.begin(); itr!=grass_h.end() && !stop; ++itr) 
    {
      int h = *itr;
      int count = grass_count.count(h); 

      for (int row=0; row<N && count > 0 && !stop; row++) {
        for (int col=0; col<M && count > 0 && !stop; col++) {
          if (table[row][col] < 0 || table[row][col] != h) continue;

          int found_in_row = check_row(row, col, N, M, table, h);
          if (found_in_row >= 0) {
            mark_row(row, col, N, M, table ,h);
            count = count - found_in_row;
          } else  { // row not possible

            int found_in_col = check_col(row, col, N, M, table, h);
            if (found_in_col < 0) { // col also not possible
              stop = true;
              ans = false;
              break;
            }

            mark_col(row, col, N, M, table ,h);
            count = count - found_in_col;
          }

        }
      } 

      /*for (int row=0; row<N; row++) {
        for (int col=0; col<M; col++) {
          cout << table[row][col] << " ";
        }
        cout << endl;
      }
      cout << "============" << endl;*/
    }

    // Free memory
    for (int row=0; row<N; row++) {
      delete []table[row];
    }
    delete []table;

    // Print answer
    cout << "Case #" << i << ": ";
    if (ans) {
      cout << "YES" << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}

