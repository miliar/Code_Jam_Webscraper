#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <math.h>

using std::cin;
using std::cout;
using std::endl;
using std::vector;

void print_tiles(const vector<long long> &tiles) {
  if (tiles.size() > 0)
  {
    for (int i = 0; i < tiles.size(); ++i)
    {
      cout << tiles[i] << " ";
    }
  } else {
    cout << "IMPOSSIBLE";
  }
  cout << endl;
}

vector<long long> tiles_for_artwork(int K, int C, int S) {
  int sequence_size = pow(K, C), original_sequences = pow(2, K);


  vector<long long> tiles;
  if (K == S)
  {
    for (int i = 0; i < S; ++i)
    {
      tiles.push_back(i + 1);
    }
  }

  return tiles;
}

int main() {

  int T = 0, K = 0, S = 0, C = 0;

  cin >> T;
  vector<long long> tiles;
  for (int i = 0; i < T; ++i)
  {
    cin >> K >> C >> S;
    tiles = tiles_for_artwork(K, C, S);

    cout <<  "Case #" << i + 1 << ": ";
    print_tiles(tiles);
  }

  return 0;
}
