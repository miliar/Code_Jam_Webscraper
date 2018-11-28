#include <climits>
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

#define MAX_R (16)

int grid[MAX_R+2][MAX_R+2];
int R, C, N;

int count_unhappiness() {
  /*for (int r=1; r<=R; r++) {
    for (int c=1; c<=C; c++) {
      cout << grid[r][c] << ", ";
    }
    cout << "\n";
    }*/
  int u = 0;
  for (int r=1; r<=R; r++) {
    for (int c=1; c<=C; c++) {
      if (grid[r][c]) {
        //cout << "r, c " << r << ", " << c << "\n";
        u += grid[r+1][c] + grid[r][c+1];
      }
      //cout << "u " << u << "\n";
    }
  }
  //cout << "count: " << u << "\n";

  return u;
}

// t from 0 to R*C-1
pair<int, int> decode(int t) {
  //cout << "decode " << t << " : " << t/C + 1<< ", " << t%C + 1<< "\n";
  return make_pair(t/C + 1, t%C + 1);
}

void put_neigh(int i, int next_a, int &min_un) {
  if (i==N) {
    int cur = count_unhappiness();
    min_un = (cur < min_un ? cur : min_un);
    return;
  }
  for (int j = next_a; j < R*C; j++) {
    //cout << "kita\n";
    pair<int, int> cor = decode(j);
    grid[cor.first][cor.second] = 1;
    put_neigh(i+1, j+1, min_un);
    grid[cor.first][cor.second] = 0;
  }
}

int solve() {
  int min_un = INT_MAX;
  //for (int i=0; i<R*C; i++) {
    put_neigh(0, 0, min_un);
    //}
  return min_un;
}

int main() {
  vector<int> result;

  int tests;
  cin >> tests;

  for (int t=0; t<tests; t++) {
    cin >> R >> C >> N;
    result.push_back(solve());
  }

  for (int i=0; i<int(result.size()); i++) {
    cout << "Case #" << i+1 << ": " << result[i] << "\n";
  }
  return 0;
}
