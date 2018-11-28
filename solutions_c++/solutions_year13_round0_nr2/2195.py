#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {

  ifstream I((argc == 1) ? ("sample_input.txt") : (argv[1]));
  ofstream O("output.txt");
  string line;

  int T; I >> T;

  for (int t = 0; t < T; ++t) {

    int N, M; I >> N >> M;

    vector<short> rows(N + 1, 0);
    vector<short> cols(M + 1, 0);

    vector<vector<pair<short, short> > > heights(101);

    short max_h = 0;
    for (int n = 1; n <= N; ++n) {
      for (int m = 1; m <= M; ++m) {
        short h; I >> h;

        heights[h].push_back(pair<short, short>(n, m));

        if (rows[n] < h) rows[n] = h;
        if (cols[m] < h) cols[m] = h;

        if (max_h < h) max_h = h;
      }
    }


    bool possible = true;

    for (int h = max_h; h > 0 && possible; --h) {

      if (heights[h].empty())
        continue;

      for (size_t i = 0; i < heights[h].size(); ++i) {

        short n = heights[h][i].first;
        short m = heights[h][i].second;

        if (h < rows[n] && h < cols[m]) {
          possible = false;
          break;
        }
      }
    }


    O << "Case #" << (t + 1) << ": " << ((possible) ? ("YES") : ("NO")) << endl;
  }

  I.close();
  O.close();

  return 0;
}
